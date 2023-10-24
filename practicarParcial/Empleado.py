from abc import abstractclassmethod

# Clase Empleado:

# Atributos: nombre, apellido, sueldo.
# Métodos: calcular_salario().


class Empleado():

    sueldoBase = 5000

    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevoNombre):
        self.__nombre = nuevoNombre

    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self,nuevoApellido):
        self.__apellido = nuevoApellido

    @abstractclassmethod
    def calcular_salario(self):
        pass