numeros_del_usuario = []
numero_del_usuario = ""

while len(numeros_del_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_del_usuario.append(int(numero_del_usuario))
    print("Numero añadido")
    numero_del_usuario = ""

numero_grande = numeros_del_usuario[0]

for numero in numeros_del_usuario:
    if numero > numero_grande:
        numero_grande = numero

print("El numero mas grande es: {}".format(numero_grande))


