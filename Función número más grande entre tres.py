def numero_mas_grande_entre_tres(primero, segundo, tercero):
    if primero >= segundo:
        numero_proceso = primero
    else:
        numero_proceso = segundo
    if tercero >= numero_proceso:
        numero_mas_grande = tercero
    else:
        numero_mas_grande = numero_proceso
    return numero_mas_grande


primer_numero = int(input("Dime un numero: "))
segundo_numero = int(input("Dime un numero: "))
tercero_numero = int(input("Dime un numero: "))

bigger_numero = numero_mas_grande_entre_tres(primer_numero, segundo_numero, tercero_numero)
print(f"Este es el número más grande: {bigger_numero}")
