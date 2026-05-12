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

print(zombie.get_type_of_enemy())
