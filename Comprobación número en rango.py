def numero_en_rango(numero_solo, numero_rango_1, numero_rango_2):
    if numero_solo in range(numero_rango_1, numero_rango_2):
        esta_numero_en_rango = True
    else:
        esta_numero_en_rango = False
    return esta_numero_en_rango


numero_a_comprobar = int(input("Dime el número que deseas comprobar: "))
primer_numero_en_rango = int(input("Dime el primer número en el rango: "))
segundo_numero_en_rango = int(input("Dime el segundo número en el rango: "))

respuesta = numero_en_rango(numero_a_comprobar, primer_numero_en_rango, segundo_numero_en_rango)

if respuesta:
    print("El número SI está en el rango")
else:
    print("El número NO está en el rango")




