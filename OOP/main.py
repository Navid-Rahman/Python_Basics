from enemy import *
from ogre import *
from zombie import *


def battle(e: Enemy):
    e.talk()
    e.attack()


zombie = Zombie(
    health_points=50,
    attack_damage=9
)

ogre = Ogre(
    health_points=75,
    attack_damage=12
)

battle(zombie)
battle(ogre)
