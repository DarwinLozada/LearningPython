# Elegimos contra que pokemon queremos luchar

pokemon_elegido = input("¿Contra qué pokemon deseas luchar? Squirtle/Charmander/Bulbasur")

nombre_pokemon = " "
vida_pikachu = 100
vida_enemigo = 0
ataque_enemigo = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
elif pokemon_elegido == "Bulbasur":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasur"
elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"

if pokemon_elegido == "Squirtle":
    ataque_enemigo = 10
elif pokemon_elegido == "Charmander":
    ataque_enemigo = 12
elif pokemon_elegido == "Bulbasur":
    ataque_enemigo = 9

while vida_pikachu > 0 and vida_enemigo > 0:
    print("Codigo Combate")
    ataque_elegido = input("¿Qué ataque eliges? (Ataque Chispazo o Bola Voltio o Mordisco)")
    if ataque_elegido == "Ataque Chispazo":
        vida_enemigo -= 10
        print("{} ha sufrido 10 de daño".format(nombre_pokemon))
    if ataque_elegido == "Bola Voltio":
        vida_enemigo -= 12
    if ataque_elegido == "Mordisco":
        vida_enemigo -= 7
        print("{} ha sufrido 12 de daño".format(nombre_pokemon))
    print("La vida de {} es de {}".format(nombre_pokemon, vida_enemigo))
    vida_pikachu -= ataque_enemigo
    print("Pikachu ha sufrido daño, ahora tiene {} de vida ".format(vida_pikachu))

if vida_pikachu == 0 or vida_pikachu < 0:
    print("Haz perdido :c")
if vida_enemigo == 0 or vida_enemigo < 0:
    print("Felicidades, has ganado")
