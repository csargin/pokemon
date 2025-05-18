import pygame
from player import Player
from game_state import GameState, CurrentGameState
from game_view.map import Map
from monsterfactory import MonsterFactory
import config
import math
import utilities
from game_view.battle import Battle
from utilities import test_if_int

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.current_game_state = CurrentGameState.MAP
        self.player_has_moved = False
        self.monster_factory = MonsterFactory()
        self.map = Map(screen)
        self.maps = [self.map]
        self.battle = None
        
    def set_up(self):
        player = Player(1,1)
        self.player = player
        self.objects.append(player)
        print("Game set up")
        self.game_state = GameState.RUNNING 
        self.map.load("01")       
        
    def update(self):
        if self.current_game_state == CurrentGameState.MAP:
            self.player_has_moved = False
            
            self.screen.fill(config.BLACK)
            self.handle_events()
            self.map.render(self.screen,self.player, self.objects)   
            
            if self.player_has_moved:
                self.determine_game_events()
        elif self.current_game_state == CurrentGameState.BATTLE:
            self.battle.update()
            self.battle.render()

            if self.battle.monster.health <= 0:
                print("Monster died")
                self.battle.monster.health = 0
                self.current_game_state = CurrentGameState.MAP

    def determine_game_events(self):
        map_tile = self.map.map_array[self.player.position[1]][self.player.position[0]]
        print(map_tile)

        if map_tile == config.MAP_TILE_ROAD:
            return
        # check if tile is a door
        elif test_if_int(map_tile):
            room = Map(self.screen)
            room.load_room(self.map.file_name, map_tile, self.player)
            self.map = room
            self.maps.append(room)
            return

        else:
            if self.player.monsters:
                self.determine_pokemon_encounter(map_tile)
        
    def determine_pokemon_encounter(self,map_tile):
        # Randomly determine if a Pokemon appears
        random_number = utilities.generate_random_number(1,10)
        
        if random_number <= 2:
            found_monster = self.monster_factory.create_monster(map_tile)
            print("You have encountered a wild " + found_monster.type + " Pokemon !")

            self.battle = Battle(self.screen, found_monster, self.player)
            self.current_game_state = CurrentGameState.BATTLE
 
          

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
                print("Game ended")
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.NONE
                    print("Game Paused")
                    
                elif event.key == pygame.K_w: # Move up
                    self.move_unit(self.player,[0 , - 1])
                elif event.key == pygame.K_s: # Move down
                    self.move_unit(self.player,[0 , 1])
                elif event.key == pygame.K_a: # Move left
                    self.move_unit(self.player,[-1 , 0])
                elif event.key == pygame.K_d: # Move right
                    self.move_unit(self.player,[1 , 0])
                    

        
    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        # Check if the new position is within the bounds of the map
        if new_position[0] < 0 or new_position[0] >= len(self.map.map_array[0]):
            return
        if new_position[1] < 0 or new_position[1] >= len(self.map.map_array):
            return
        
        # Check if the new position is a valid tile
        if self.map.map_array[new_position[1]][new_position[0]] in config.IMPASSIBLE:
            return
                
        self.player_has_moved = True
        
        unit.update_position(new_position)
        





  