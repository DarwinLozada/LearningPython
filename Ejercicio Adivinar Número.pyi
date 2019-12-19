
numero_a_adivinar = int(input("Escribe el número a adivinar (el programa no finalizará hasta que se de con dicho dígito)"))
respuesta_al_numero = int(input("¿Qué número crees que sea el correcto?"))

while numero_a_adivinar != respuesta_al_numero:
    print("Lo siento, te has equivocado")
    respuesta_al_numero = int(input("¿Qué número crees que sea el correcto?"))

print("Así es, era {})").format(numero_a_adivinar)