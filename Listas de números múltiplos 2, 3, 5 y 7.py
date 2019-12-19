lista_numeros_usuario = []
numero_agregado = ""

print("Escribir -Finalizar- para detener el programa")

while not numero_agregado == "Finalizar":
    numero_agregado = input("Dime un numero: ")
    if numero_agregado.isdigit():
            lista_numeros_usuario.append(numero_agregado)
            print("Número añadido")

lista_multiplos_2 = []
lista_multiplos_3 = []
lista_multiplos_5 = []
lista_multiplos_7 = []

for indice in range(len(lista_numeros_usuario)):
    numero = int(lista_numeros_usuario[indice])
    if numero % 2 == 0:
        lista_multiplos_2.append(numero)
    if numero % 3 == 0:
        lista_multiplos_3.append(numero)
    if numero % 5 == 0:
        lista_multiplos_5.append(numero)
    if numero % 7 == 0:
        lista_multiplos_7.append(numero)

print(f"Los múltiplos de 2 son: {lista_multiplos_2}")
print(f"Los múltiplos de 3 son: {lista_multiplos_3}")
print(f"Los múltiplos de 5 son: {lista_multiplos_5}")
print(f"Los múltiplos de 7 son: {lista_multiplos_7}")