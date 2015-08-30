# monsters 
import random

monsters = {
    'skeleton': 2,
    'zombie': 3,
    'spider': 1
    }

def get_monster():
    monster = random.choice(monsters.keys())
    monster_lives = monsters[monster]
    return monster, monster_lives

get_monster()

