from hero import *
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


def hero_battle(hero: Hero, enemy: Enemy):
    while hero.health_points > 0 and enemy.health_points > 0:
        print("__________________")

        print(f"Hero: {hero.health_points} HP left")
        print(f"{enemy.get_type_of_enemy()}: {enemy.health_points} HP left")

        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print("_______________")
    if hero.health_points > 0:
        print(f"Hero wins!!!")
    else:
        print(f"{enemy.get_type_of_enemy()} wins!!!")


zombie = Zombie(
    health_points=10,
    attack_damage=1
)

ogre = Ogre(
    health_points=20,
    attack_damage=3
)

hero = Hero(
    health_points=10,
    attack_damage=1
)

weapon = Weapon(
    weapon_type="Sword",
    attack_increase=5
)

hero.weapon = weapon
hero.equip_weapon()

hero_battle(hero, ogre)
