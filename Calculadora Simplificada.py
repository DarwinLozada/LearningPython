primer_numero = 0
segundo_numero = 0

operacion_a_realizar = input("¿Qué operación desea realizar? Multiplicación/División/Suma/Resta")

if operacion_a_realizar == "Multiplicación":
    primer_numero = int(input("Número a multiplicar"))
    segundo_numero = int(input("Número que multiplica"))
    resultado = primer_numero * segundo_numero
    print("El resultado es {}".format(resultado))

elif operacion_a_realizar == "División":
    primer_numero = int(input("Número a dividir"))
    segundo_numero = int(input("Número que divide"))
    resultado = primer_numero / segundo_numero
    print("El resultado es {}".format(resultado))

elif operacion_a_realizar == "Suma":
        primer_numero = int(input("Primer factor"))
        segundo_numero = int(input("Segundo factor"))
        resultado = primer_numero + segundo_numero
        print("El resultado es {}".format(resultado))

elif operacion_a_realizar == "Resta":
    primer_numero = int(input("Número a restar"))
    segundo_numero = int(input("Número que resta"))
    resultado = primer_numero - segundo_numero
    print("El resultado es {}".format(resultado))
