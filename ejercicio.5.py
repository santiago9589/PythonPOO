#Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas, minutos y segundos


def calcularDuracionSegundos(hora,minutos,segundos):

    if (hora > 0 and hora<61) and (minutos > 0 and minutos<61) and (segundos > 0 and segundos<61) :

        hora = hora * 3600
        minutos = minutos * 60
        return f"el total en segundos es {hora + minutos + segundos}"
    else:
        return "hubo un error en los datos ingresados"

fuc = calcularDuracionSegundos(1,1,1)

print(fuc)

