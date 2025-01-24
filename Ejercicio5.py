numero = int(input("Intruduzca un numero para comprobar si es par o impar: "))
comprobar = numero % 2

if comprobar == 0:
    print("El número", numero, "es par")
else:
    print("es impar")