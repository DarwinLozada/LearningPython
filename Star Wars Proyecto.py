def direccion_moverse(d):
    if d == 0:
        direccion = "Up"
    if d == 1:
        direccion = "Right"
    if d == 2:
        direccion = "Down"
    if d == 3:
        direccion = "Left"


class Stardestroyer:
    def __init__(self, d):
        self.d = d


class Naveusuario:
    def __init__(self, escudo, combustible, sobrevivientes):
        self.escudo = escudo
        self.combustible = combustible
        self.sobrevivientes = sobrevivientes

        pass





def main():
    matriz = []
    anadir_matriz = []
    numero_filas = int(input(""))
    if numero_filas < 4 or numero_filas > 4:
        print("NO VALIDO")
        exit()
    else:
        numero_columnas = int(input(""))
        for i in range(numero_filas):
            anadir_matriz = input("")
        anadir_matriz.append("\n")
        



    for i in range(numero_filas):
        matriz.append(".")
    for j in range(numero_columnas):
        print(matriz)
    matriz = input("")





if __name__ == "__main__":
    main()






