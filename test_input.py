apetece_helado_input = input("¿Te apetece un helado? (Si / No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que respondieras con si o no")
    apetece_helado = False

tiene_dinero_input = input("¿Tienes dinero para un helado? (Si / No): ").upper()
if tiene_dinero_input == "SI":
    tiene_dinero_input = True
elif tiene_dinero_input == "NO":
    tiene_dinero_input = False
else:
    print("Te he dicho que respondieras con si o no")
    tiene_dinero_input = False

esta_el_senor_de_los_helados_input = input("¿Esta el señor de los helados? (Si / No): ").upper()
if esta_el_senor_de_los_helados_input == "SI":
    esta_el_senor_de_los_helados_input = True
elif esta_el_senor_de_los_helados_input == "NO":
    esta_el_senor_de_los_helados_input = False
else:
    print("Te he dicho que respondieras con si o no")
    esta_el_senor_de_los_helados_input = False

esta_tu_tia_input = input("¿Estás con tu tía? (Si / No): ").upper()
if esta_tu_tia_input == "SI":
    esta_tu_tia_input = True
elif esta_tu_tia_input == "NO":
    esta_tu_tia_input = False
else:
    print("Te he dicho que respondieras con si o no")
    esta_tu_tia_input = False


tiene_dinero = tiene_dinero_input == "SI"
esta_tu_tia = esta_tu_tia_input == "SI"
puede_permitirselo = tiene_dinero or esta_tu_tia
esta_el_senor_de_los_helados = esta_el_senor_de_los_helados_input == "SI"

if  apetece_helado and puede_permitirselo and esta_el_senor_de_los_helados:
    print("Pues comete un helado")
else:
    print("Pues nada")



