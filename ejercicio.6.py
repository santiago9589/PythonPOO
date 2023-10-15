#Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados 
#en horas, minutos y segundos, sume sus duraciones, 
#y muestre por pantalla la duración total en horas, minutos y segundos.

def parsearValores(stringIngresado):
    listNueva = []
    for n in stringIngresado:
        listNueva.append(int(n))
    return listNueva

def verificacionValor(valorIngresado):
    hora,minutos,segundos = valorIngresado
    return (hora > 0 and hora<61) and (minutos > 0 and minutos<61) and (segundos > 0 and segundos<61) 

def calcularSumaIntervalos(primerIntervaloF,segundoIntervaloF):
    listIngresada1 = parsearValores(primerIntervaloF)
    listIngresada2 = parsearValores(segundoIntervaloF)
    if verificacionValor(listIngresada1) and verificacionValor(listIngresada2):
        hora = listIngresada1[0] + listIngresada2[0]
        minutos = listIngresada1[1] + listIngresada2[1]
        segundos = listIngresada1[2] + listIngresada2[2]
        return f"la suma de los intervalos es horas : {hora} , minutos: {minutos} , segundos: {segundos} "
    else:   
        return f"hubo un error en los datos ingresados"
    
primerIntervalo = input("ingrese primer intervalo (horas,minutos,segundos): ")
segundoIntervalo = input("ingrese segundo intervalo (horas,minutos,segundos) : ")

lista1 = primerIntervalo.split(",")
lista2 = segundoIntervalo.split(",")

func = calcularSumaIntervalos(lista1,lista2)
print(func)