# Ejercicio POO con encapsulamiento y uso de atributos de instancia y de clase
# Crear una clase llamada Password con las siguientes condiciones:
# • Dos atributos de clase privados:
# 1. LONGITUD. Cuyo valor sea 8 (numérico).
# 2. CARACTERES_VALIDOS. Cuyo valor sea
# "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%
# &+" (string)
# • Dos atributos de instancia privados:
# 1. longitud. Por defecto, será igual al valor del atributo de clase LONGITUD. Y su valor no
# podrá ser inferior a 6 caracteres ni mayor a 15 caracteres.
# 2. contraseña. Su valor aleatorio deberá ser asignado en el método generarPassword().
# • Un método inicializador de instancias, con el parámetro longitud cuyo valor se asignará al
# atributo de instancia. Generará una contraseña aleatoria con esa longitud invocando al
# método generarPassword().
# • Dos métodos de instancia públicos, cuya implementación deberá ser:
# 1. esFuerte(): devuelve un booleano si es fuerte o no. Para que sea fuerte debe tener
# más de 1 mayúscula, 1 carácter especial, más de 1 minúscula y más de 1 números.
# 2. generarPassword(): genera la contraseña del objeto cuyo valor de tipo string tendrá
# una longitud igual al valor del atributo de instancia “longitud”. Para la generación de la
# clave puede usar los métodos random.choice() y string.join() de Python.
# • Incluir métodos públicos que permitan obtener y asignar valores (getters y setters) a los
# atributos de instancia privados.
# • Sobreescribir el método de instancia __str__(), para que retorne la clave generada y el
# valor booleano que devuelve el método “es_fuerte()”.
# Luego, agregar sentencias de código Python que permitan:
# • Crear una lista de objetos de tipo Password.
# • Crear instancias de Password y agregarlas a la lista. Para cada objeto, se debe ingresar la
# longitud de la clave por teclado. Si el valor ingresado es cero, no se pasará ningún valor
# como argumento al método inicializador.
# • Mostrar cada una de las contraseñas creadas y si es o no fuerte (usar un bucle). Para ello,
# usar este simple formato:
# contraseña1 - valor_booleano1
# contraseña2 - valor_bololeano2

import random


class Password():

    __LONGITUD = 8
    __CARACTERES_VALIDOS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%#&+"

    def __init__(self,longitud = None):
        self.__longitud = longitud or self.__LONGITUD
        self.__contraseña = self.generarPassword()

    def getLongitud(self):
        return self.__longitud
    
    def setLongitud(self,nuevaLongitud):
        if(nuevaLongitud > 5 and nuevaLongitud < 16):
            self.__longitud = nuevaLongitud

    def getContraseña(self):
        return self.__contraseña
    
    def setContraseña(self,nuevaContraseña):
       if(nuevaContraseña.len > self.getLongitud()):
            self.__contraseña = nuevaContraseña

    def esFuerte(self):
       
       contadorLower = 0
       contadorUpper = 0
       contardorEspeciales = 0
       contadorNumeros = 0

       for caracter in self.getContraseña():
            if caracter.islower():
                contadorLower += 1
            else:
                if caracter.isupper():
                    contadorUpper+= 1
                else:
                    if not caracter.isalnum():
                        contardorEspeciales+= 1
                    else:
                        if caracter.isdigit():
                            contadorNumeros+= 1

            return contadorLower > 1 and contadorNumeros > 1 and contardorEspeciales > 1 and contadorUpper > 1


    def generarPassword(self):
        
        contraseñaNueva = ""

        for numero in range(0, self.getLongitud()):
            contraseñaNueva += random.choice(self.__CARACTERES_VALIDOS)
            
        return contraseñaNueva


    def __str__(self):
        return f"{self.getContraseña()} - {self.esFuerte()} "