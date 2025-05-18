import random
import pygame
import config
import math
import utilities

from player import Player
from game_state import GameState

class Menu:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def set_up(self):
        self.menu_img = pygame.image.load(config.MENU_IMAGE_PATH)
        self.menu_img = pygame.transform.scale(self.menu_img, (800, 600))

    def update(self):
        self.screen.fill(config.BLACK)
        rect = pygame.Rect(1, 1, 2, 2)
        self.screen.blit(self.menu_img, rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
                print("Game ended")
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.RUNNING
                    print("Game unpaused")
                    
                elif event.key == pygame.K_RETURN:
                    self.game.game_state = GameState.RUNNING
                    print("Game started")
                    self.game.set_up()