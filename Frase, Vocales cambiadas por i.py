frase_usuario = input("Dime una frase: ")

for vocal in list("aeiouAEIOU"):
    frase_usuario = frase_usuario.replace(vocal, "i")

print(frase_usuario)