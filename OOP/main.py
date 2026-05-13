from ogre import *
from zombie import *

zombie = Zombie(
    health_points=50,
    attack_damage=9
)

ogre = Ogre(
    health_points=75,
    attack_damage=12
)

print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and {zombie.attack_damage} attack damage')
print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and {ogre.attack_damage} attack damage')

zombie.talk()
ogre.talk()
