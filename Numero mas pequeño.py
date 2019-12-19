numeros_del_usuario = []
numero_del_usuario = ""

while len(numeros_del_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_del_usuario.append(int(numero_del_usuario))
    print("Numero añadido")
    numero_del_usuario = ""

numero_mas_pequeno = numeros_del_usuario[0]

for numero in numeros_del_usuario:
    if numero < numero_mas_pequeno:
        numero_mas_pequeno = numero

print("Este es el numero mas pequeño: {}".format(numero_mas_pequeno))
