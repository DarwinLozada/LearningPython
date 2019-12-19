numero_tabla = int(input("De que numero desea saber la tabla del 5 al 15: "))

for multiplo in range(5, 16):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))

