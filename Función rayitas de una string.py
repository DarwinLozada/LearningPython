def rayitas_de_una_string(string):
    string_rayitas = ""

    for letra in string:
        string_rayitas += "-"
    return string_rayitas


frase_usuario = input("Dime una frase: ")
print(rayitas_de_una_string(frase_usuario))
