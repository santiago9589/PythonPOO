#Escribe un programa en Python que solicite al usuario que ingrese 5 números enteros. Luego imprimir el máximo
#y el mínimo de los valores ingresados. El programa deberá permitir el ingreso de valores iguales

listaNumero = [];


for i in range (5):
    numeroIngresado = int(input(f"ingrese un numero entero : "))
    listaNumero.append(numeroIngresado)
   
numeroMaximo = max(listaNumero)
numeroMinimo = min(listaNumero)

print(f"El numero maximo es {numeroMaximo} y el minimo es {numeroMinimo}")