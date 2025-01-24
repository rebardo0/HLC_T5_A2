numeros_serie_Fibonacci = [0, 1]

for i in range(2, 10):
    siguiente_numero = numeros_serie_Fibonacci[i-1] + numeros_serie_Fibonacci[i-2]
    numeros_serie_Fibonacci.append(siguiente_numero)

print(numeros_serie_Fibonacci)