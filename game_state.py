from enum import Enum

class GameState(Enum):
    """Enum representing the state of the game."""
    NONE = 0, # No state
    RUNNING = 1, # Game is running
    ENDED = 2, # Game has ended
    MAP = 3, # Game is on the map
    BATTLE = 4, # Game is in the pokemon battle
    INVENTORY = 5, # Game is in the inventory
    STORE = 6, # Game is in the store
    MENU = 7, # Game is in the menu
    SETTINGS = 8, # Game is in the settings

class CurrentGameState(Enum):
    """Enum representing the state of the game."""
    NONE = 0, # No state
    MAP = 1, # Game is on the map
    BATTLE = 2, # Game is in the pokemon battle
    INVENTORY = 3, # Game is in the inventory
    STORE = 4, # Game is in the store
    MENU = 5, # Game is in the menu
    SETTINGS = 6, # Game is in the settings