frase_del_usuario = input("Introduzca una frase: ")

mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numero_mayusculas = 0

for letras in frase_del_usuario:
    if letras in mayusculas:
        numero_mayusculas += 1

print("El número de mayúsculas son: {}".format(numero_mayusculas))