from pokemon_combat.pokemon_combat_classes import Pikachu, Squirtle, Charmander, Bulbasur


def choose_enemy():
    pokemon = input("Against which pokemon do you wanna fight? Squirtle/Charmander/Bulbasur ")
    if pokemon == "Squirtle":
        return Squirtle()
    elif pokemon == "Bulbasur":
        return Bulbasur()
    elif pokemon == "Charmander":
        return Charmander()
    elif pokemon == "Pikachu":
        return Pikachu()


def main():
    pikachu = Pikachu()
    enemy = choose_enemy()

    while not enemy.base_health <= 0 and not pikachu.base_health <= 0:
        chosen_attack = input("\nChoose your attack (Chispazo o Bola Voltio) ")
        pikachu.attack(enemy, chosen_attack)

        enemy.show_health()
        enemy.attack(pikachu)

        pikachu.show_health()

    if enemy.base_health <= 0:
        print("\nFelicidades, has ganado")

    elif pikachu.base_health <= 0:
        print("\nHaz perdido :c")


if __name__ == '__main__':
    main()
