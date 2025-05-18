from monster import Monster
import utilities
import config
import configmonster

class MonsterFactory:
    def __init__(self):
        self.count = 0
 
    def create_monster(self, monster_type):
        """Create a new monster of the specified type."""
        
        random_number = -1
        
        if monster_type == config.MAP_TILE_GRASS:
            random_number = utilities.generate_random_number(configmonster.GRASS_TYPE_START, configmonster.GRASS_TYPE_END)            

        elif monster_type == config.MAP_TILE_WATER:
            random_number = utilities.generate_random_number(configmonster.WATER_TYPE_START, configmonster.WATER_TYPE_END)            
         
        monster = Monster(monster_type, random_number)
        self.count += 1

        return monster