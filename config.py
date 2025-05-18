
#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

SCALE = 32 # Scale factor for the game
FPS = 50 # Frames per second for the game

SCREEN_WIDTH = 640 # Width of the game screen
SCREEN_HEIGHT = 480 # Height of the game 

PLAYER_IMAGE_PATH = "pokemon/imgs/player.png" # Path to the player image
MAP_PATH = "pokemon/maps/" # Path to the maps folder
MAP_IMAGE_PATH = "pokemon/imgs/" # Path to the map image
MENU_IMAGE_PATH = "pokemon/imgs/menu.png" # Path to the menu image
MONSTER_PATH = "pokemon/imgs/monsters/" # Path to the monster folder

MAP_TILE_WATER = "W" # Water tile
MAP_TILE_GRASS = "G" # Grass tile
MAP_TILE_ROAD = "R" # Road tile
MAP_TILE_DOOR = "1" # Door tile
MAP_TILE_DOORS = ["1", "2", "3", "4", "5", "6", "7", "8"] # Door tileS
MAP_TILE_LAB_FLOOR = "L" # Lab floor tile
MAP_TILE_LAB_WALL = "l" # Lab wall tile
MAP_TILE_ROOM_EXIT = "X" # Room exit tile
MAP_TILE_BUILDING = "." # Building tile

MONSTER_TYPES = ["G", "W", "S", "F"]

IMPASSIBLE = [MAP_TILE_WATER, MAP_TILE_LAB_WALL, MAP_TILE_BUILDING]

MAP_CONFIG = {
    "01" : {
        "start_position": [9, 29],
        "exits" : [
        {
            "map" : "02",
            "position" : [3, 0],
            "new_start_position": [1, 4],
        }],
        "buildings": [
            {
                "sprite": "04",
                "name": "Research Building",
                "position": [10, 2],
                "size" : [4, 5]
            },
            {
                "sprite": "05",
                "name": "Home",
                "position": [6, 26],
                "size" : [5, 3]
            }
        ],
    },
    "02" : {
        "start_position": [1, 4],
        "exits" : [{
            "map" : "01",
            "position" : [1, 5],
            "new_start_position" : [3, 1],
        }],
        "buildings": [
        ],
    }
}

ROOM_CONFIG = {
    "01" : {
        "01" : {
            "start_position" : [10,13],
            "exit_position" : [12,7],
            "npcs" : [
                {
                    "name" : "prof",
                    "image" : "prof",
                    "start_position" : [8,8]
                },
                {
                    "name" : "monster_cage_starter_01",
                    "image" : "monster_cage_starter_1",
                    "start_position": [10, 8]
                },
                {
                    "name" : "monster_cage_starter_02",
                    "image": "monster_cage_starter_2",
                    "start_position": [11, 8]
                },
                {
                    "name" : "monster_cage_starter_03",
                    "image": "monster_cage_starter_3",
                    "start_position": [12, 8]
                }
            ]
        },
        "02" : {
            "start_position" : [10,13],
            "exit_position" : [12,7],
            "npcs" : [],
        }
    }
}

