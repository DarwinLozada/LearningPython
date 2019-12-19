numero_tabla = int(input("De que numero desea ver la tabla: "))

for multiplo in range(1, 13):
    if multiplo % 2 == 0:
        print("{} x {} = {}".format(numero_tabla, multiplo, multiplo*numero_tabla))
        


