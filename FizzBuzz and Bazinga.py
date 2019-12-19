lista_numeros = []
respuesta_usuario = ""

print("Escribir -Finalizar- para detener el programa")

while not respuesta_usuario == "Finalizar":
    respuesta_usuario = (input("Dime un número"))
    if not respuesta_usuario == "Finalizar":
        lista_numeros.append(int(respuesta_usuario))
        print("Número añadido")

for indice in range(len(lista_numeros)):
    numero = int(lista_numeros[indice])
    if numero % 3 == 0 and numero % 5 == 0:
        lista_numeros[indice] = "Bazinga"
    elif numero % 3 == 0:
        lista_numeros[indice] = "Fizz"
    elif numero % 5 == 0:
        lista_numeros[indice] = "Buzz"
    else:
        lista_numeros[indice] = "No múltiplo de 2 ni 3"


print(lista_numeros)