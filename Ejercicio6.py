palabra = input("Introduzca una palabra para verificar: ")
caracteres = ["@", "#", "$", "%"]

for caracter in caracteres:
    if caracter in palabra:
        print("La palabra tiene el caracter: ", caracter)
    else:
        print("La palabra no tiene el caracter: ", caracter)