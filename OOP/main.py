from enemy import *

zombie = Enemy(
    type_of_enemy="zombie",
    health_points=100,
    attack_damage=9
)

yeti = Enemy(
    type_of_enemy="yeti",
    health_points=100,
    attack_damage=10
)

# print(f'{enemy.type_of_enemy} has {enemy.health_points} health points and can do an attack of {enemy.attack_damage} damage.')
yeti.talk()
