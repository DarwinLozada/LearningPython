lista_numeros = []
numeros_agregar = 0
print("Cuando ya no desees agregar otro numero escribe: Finalizar ")

while not numeros_agregar == "Finalizar":
    numeros_agregar = input("Dime un numero: ")
    if numeros_agregar.isdigit():
        lista_numeros.append(numeros_agregar)
        print("Número añadido")

resultado = 1

for numero in lista_numeros:
    resultado *= int(numero)

print("El resultado de la multiplicación es {}".format(resultado))