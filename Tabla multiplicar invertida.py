numero_tabla = int(input("De que numero desea ver la tabla: "))

for multiplo in range(10, 0, -1):
     print("{} x {} = {}".format(numero_tabla, multiplo, multiplo*numero_tabla))
