palabras_veces = dict()

string_usuario = input("Dime una frase: ").split()

for palabra in string_usuario:
    palabras_veces[palabra] = string_usuario.count(palabra)

print(palabras_veces)