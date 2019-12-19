numeros_del_usuario = []
numero_del_usuario = "0"

print("Cuando desee finalizar el programa escriba: Finalizar")

while not numero_del_usuario == "Finalizar":
    numero_del_usuario = input("Dime un numero: ")
    if numero_del_usuario.isdigit():
            numeros_del_usuario.append(numero_del_usuario)
            print("Número añadido")

numeros_de_la_lista = 0

for numero in numeros_del_usuario:
    numeros_de_la_lista += 1

print("Su lista tiene {} numeros".format(numeros_de_la_lista))



