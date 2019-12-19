lista_general = []
lista_enteros = []
lista_strings = []
dato_agregado = None

print("Para finalizar el código escriba Finalizar")

while not dato_agregado == "Finalizar":
    dato_agregado = input("Dime un número o una frase: ")
    if not dato_agregado == "Finalizar":
        lista_general.append(dato_agregado)
        print("Dato agregado")

for dato in lista_general:
    if dato.isdigit():
        lista_enteros.append(dato)
    elif isinstance(dato, str):
        lista_strings.append(dato)

print(f"Estos son los Strings: {lista_strings} y estos son los Enteros: {lista_enteros}")


