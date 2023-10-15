#Escrib un programa enPython que solicite 5 números enteros al usuario. El mismo debe indicar si
#entre dichos valores hay números duplicados o no, imprimiendo por pantalla “HAY DUPLICADOS” o “SON TODOS
#DISTINTOS”.

listaNumero = [];


for i in range (5):
    numeroIngresado = int(input(f"ingrese un numero entero : "))
    listaNumero.append(numeroIngresado)
   
listNumeroSet = set(listaNumero)


if(len(listNumeroSet)<len(listaNumero)):
    print("HAY DUPLICADOS")
else:
    print("SON TODOS DISTINTOS")