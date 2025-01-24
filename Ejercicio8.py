numero_enteroP = int(input("Introduzca un número entero positivo para generar una lista: "))
numeros = []

for i in range(numero_enteroP):
    numeros.append((i + 1)**2)
    
print(numeros)