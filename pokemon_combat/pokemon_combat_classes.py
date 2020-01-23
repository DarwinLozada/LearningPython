from time import sleep


class BasePokemonAttack:
    damage = 0
    name = ""


class BasePokemon:
    base_health = 0
    base_damage = None
    name = None
    attacks = []

    def __init__(self):
        self.health = self.base_health

    def attack(self, enemy, attack_name=None):
        sleep(1)
        print("\n{} attacks {} with {}!".format(self.name, enemy.name, attack_name if attack_name else "base attack"))
        if not attack_name:
            enemy.take_damage(self.base_damage)
        else:
            for attack in self.attacks:
                if attack.name == attack_name:
                    enemy.take_damage(attack.base_damage)

    def take_damage(self, damage):
        self.base_health -= damage

    def show_health(self):
        print("The health of {} is {}.".format(self.name, self.base_health))


'''
    def isdefetead(self):
        return self.health <= 0
'''


class ChispazoAttack(BasePokemonAttack):
    base_damage = 12
    name = "Chispazo"


class BolaVoltioAttack(BasePokemonAttack):
    base_damage = 9
    name = "Bola Voltio"


class Charmander(BasePokemon):
    base_health = 100
    base_damage = 10
    name = "Charmander"


class Pikachu(BasePokemon):
    base_health = 120
    base_damage = 12
    name = "Pikachu"
    attacks = [ChispazoAttack, BolaVoltioAttack]


class Bulbasur(BasePokemon):
    base_health = 80
    base_damage = 7
    name = "Bulbasur"


class Squirtle(BasePokemon):
    base_health = 100
    base_damage = 3
    name = "Squirtle"
