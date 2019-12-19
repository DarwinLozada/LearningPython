lista_numeros = []
numero_agregado = ""

print("Escribir -Finalizar- para detener el programa")

while not numero_agregado == "Finalizar":
    numero_agregado = input("Dime un numero: ")
    if numero_agregado.isdigit():
            lista_numeros.append(numero_agregado)
            print("Número añadido")

numero_mas_grande = 0

for numero in lista_numeros:
    if int(numero) > int(numero_mas_grande):
        numero_mas_grande = numero

print(f"El número más grande es: {numero_mas_grande}")