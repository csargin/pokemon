#pokemon\Scripts\activate.bat
"""
This is a simple rpg game made with pygame.

https://kenney.nl/assets/sokoban
https://kenney.nl/assets/top-down-tanks-redux
https://kenney.nl/assets/rpg-base
"""

import pygame
import config
from game import Game
from menu import Menu
from game_state import GameState


pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH,config.SCREEN_HEIGHT))

pygame.display.set_caption("Pokemon")

clock = pygame.time.Clock()
game = Game(screen)

game.set_up()

menu = Menu(screen, game)
menu.set_up()

while game.game_state != GameState.ENDED:
    clock.tick(50)
    if game.game_state == GameState.NONE:
        menu.update()

    elif game.game_state == GameState.RUNNING:
        game.update()   
    

    pygame.display.flip()