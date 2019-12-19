frase_del_usuario = input("Dime una frase: ")
vocales = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

numero_aparicion = 1

for letra in frase_del_usuario:
    if letra in vocales:
        frase_del_usuario = frase_del_usuario.replace(letra, str(numero_aparicion), 1)
        numero_aparicion += 1

print(frase_del_usuario)

