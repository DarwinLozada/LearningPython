lista_strings = []
respuesta_usuario = ""

print("Escribir -Finalizar- para detener el programa")

while not respuesta_usuario == "Finalizar":
    respuesta_usuario = input("Dime una frase ")
    if not respuesta_usuario == "Finalizar":
        lista_strings.append(respuesta_usuario)
        print("Agregado")

lista_frases = []
largo_frase = 0

for frase in lista_strings:
    largo_frase = len(frase)
    lista_frases.append(largo_frase)

print(lista_frases)