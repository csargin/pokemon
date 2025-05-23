from random import randint
from random import seed

def generate_random_number(range1, range2):
    """Generate random number between range1 and range2"""
    seed()
    return randint(range1,range2)


def test_if_int(map_tile):
    """Test if value is an int"""
    try:
        int(map_tile)
        return True
    except ValueError:
        return False