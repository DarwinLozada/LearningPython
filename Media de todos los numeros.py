numeros_del_usuario = []
numero_del_usuario = ""

while not numero_del_usuario == "Finalizar":
    numero_del_usuario = input("Dime un numero: ")
    if numero_del_usuario.isdigit():
            numeros_del_usuario.append(numero_del_usuario)
            print("Número añadido")

cantidad_lista = len(numeros_del_usuario)
total_lista = 0
total_neto = 0

for numero in numeros_del_usuario:
    total_lista += int(numero)
    total_neto = total_lista / cantidad_lista

print("La media de todos los numeros de la lista es {}".format(total_neto))




