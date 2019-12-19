mi_lista = []
input_usuario = input("¿Qué necesitas comprar? Escribe LISTO para salir")

while input_usuario != "LISTO":
    mi_lista.append(input_usuario)
    input_usuario = input("¿Qué necesitas comprar? Escribe LISTO para salir")

for objeto_a_comprar in mi_lista:
    print("Tengo que comprar {}".format(objeto_a_comprar))

print("Esta es la lista de la compra")