def dibuja():
    num_estrellas = int(input("Introduce el numero de estrellas"))

    contador = 1
    estrella = "★"
    for index in range(1,num_estrellas+1):
        print(estrella*index)
        contador += 1
dibuja()