import pygame
import config


class Player:
    def __init__(self, x_position, y_position):
        print("Player created")
        self.position = (x_position, y_position)
        self.image = pygame.image.load(config.PLAYER_IMAGE_PATH)
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)   
        self.attack = 2
        self.defense = 1
        self.health = 10
        self.monster = None
        self.monsters = []
        
    def update(self):
        pass

    def update_position(self, new_position):
        self.position = ( new_position[0], new_position[1] )
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)   
        print("Player position updated to: ", self.position)


    def render(self, screen , camera ):
        self.rect = pygame.Rect(self.position[0] * config.SCALE - (camera[0] * config.SCALE), self.position[1] * config.SCALE - (camera[1] * config.SCALE), config.SCALE, config.SCALE)
        screen.blit(self.image, self.rect)
        
        