def numeros_pares_en_lista(lista_de_numeros):
    numeros_pares = []
    for numero in lista_de_numeros:
        if numero.isdigit():
            if int(numero) % 2 == 0:
                numeros_pares.append(numero)
    return numeros_pares


numero_a_agregar = ""
lista_numeros = []

while not numero_a_agregar == "Finalizar":
    numero_a_agregar = input("Dime un número: ")
    if numero_a_agregar.isdigit():
        lista_numeros.append(numero_a_agregar)
        print("Numero añadido")

pares_en_lista = numeros_pares_en_lista(lista_numeros)
print(f"Estos son los números pares en la lista {pares_en_lista}")
