import pygame
import config

class Monster:
    """A class representing monsters in the game."""
    def __init__(self, monster_type, id):
        print("Monster created")
        self.type = monster_type
        self.health = 10
        self.attack = 2
        self.defense = 1
        self.id = id
        self.image = pygame.transform.scale(pygame.image.load(config.MONSTER_PATH  + f"{self.id:03d}" + ".png") , (config.SCALE, config.SCALE))
       



       
