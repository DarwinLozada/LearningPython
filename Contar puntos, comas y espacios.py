frase_del_usuario = input("Introduzca una frase: ")

espacios = [" "]
comas = [","]
puntos = ["."]

numero_de_espacios = 0
numero_de_comas = 0
numero_de_puntos = 0

for letra in frase_del_usuario:
    if letra in espacios:
        numero_de_espacios += 1
    elif letra in comas:
        numero_de_comas += 1
    elif letra in puntos:
        numero_de_puntos += 1

print("Los espacios son {}".format(numero_de_espacios))
print("Los comas son {}".format(numero_de_comas))
print("Los puntos son {}".format(numero_de_puntos))