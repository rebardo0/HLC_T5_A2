primernumero = int(input("introduce un primer numero: "))
segundonumero = int(input("introduce un segundo numero: "))
tercernumero = int(input("introduce un tercer numero: "))

if primernumero > segundonumero and primernumero > tercernumero:
    print (primernumero ,"Es mayor" )
elif segundonumero > primernumero and segundonumero > tercernumero:
    print (segundonumero ,"Es mayor" )
elif tercernumero > primernumero and tercernumero > segundonumero:
    print (tercernumero ,"Es mayor" )
else:
    print("Si, hay un empate entre dos o más números.")