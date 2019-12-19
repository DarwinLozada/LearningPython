
amigos = dict()
accion = False

while not accion:
    accion = input("Responde [1] Para añadir un nuevo amigo, [2] Para consultar el año de nacimiento, [3] Para salir: ")
    if accion == "1":
        print("Vamos a añadir a un amigo")
        print("-------------------------")
        nombre = input("Dime el nombre: ")
        ano_de_nacimiento = input("Dime el año de nacimiento: ")
        amigos[nombre] = ano_de_nacimiento
        accion = False

    elif accion == "2":
        print("Vamos a consultar año de nacimiento")
        print("-----------------------------------")
        nombre = input("Dime el nombre: ")
        if nombre not in amigos:
            print("No hay ningún amigo agregado")
        else:
            print(f"{nombre} nació en {amigos[nombre]}")
        accion = False

    elif accion == "3":
        accion = True



