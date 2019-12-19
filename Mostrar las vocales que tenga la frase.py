frase_del_usuario = input("Escriba una frase: ")

vocales = ["a", "e", "i", "o", "u"]
lista_vocales = []

for letras in frase_del_usuario:
    if letras in vocales:
        lista_vocales.append(letras)

print("Estas son las vocales {}".format(lista_vocales))




