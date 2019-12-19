colores_ingles = {"Amarillo": "Yellow", "Rojo": "Red", "Azul": "Blue", "Verde": "Green",
                  "Morado": "Purple", "Marrón": "Brown", "Blanco": "White", "Negro": "Black",
                  "Rosado": "Pink", "Naranja": "Orange", "Azul claro": "Light blue", "Gris": "Grey"}

color_consultar = input("¿Qué color deseas saber? ")

if color_consultar in colores_ingles:
    print(f"El color {color_consultar} es {colores_ingles[color_consultar]} ")



