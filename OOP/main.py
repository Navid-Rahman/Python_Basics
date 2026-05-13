from ogre import *
from zombie import *


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print("__________________")
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left")

        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print("_______________")
    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy()} wins!!!")
    else:
        print(f"{e2.get_type_of_enemy()} wins!!!")


zombie = Zombie(
    health_points=50,
    attack_damage=9
)

ogre = Ogre(
    health_points=75,
    attack_damage=12
)

battle(zombie, ogre)
