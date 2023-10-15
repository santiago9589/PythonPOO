
from personas import Persona
from departamento import Departamento

class Empleado(Persona):
    def __init__(self, sueldo, categoria, departamento:Departamento,dni, nombre, edad, estado):
        super().__init__(dni, nombre, edad, estado)
        self.__sueldo = sueldo
        self.__categoria = categoria
        self.__departameto = departamento


    def getSueldo(self):
        return self.__sueldo
    
    def setSueldo(self,nuevoSueldo):
        self.__sueldo = nuevoSueldo

    def getCategoria(self):
        return self.__categoria
    
    def setCategoria(self,nuevaCategoria):
        self.__categoria = nuevaCategoria

    def getDepartamento(self):
        return self.__departameto
    
    def setDepartamento(self,nuevaDepartamento):
        self.__departameto = nuevaDepartamento


        
    def calcularSalarioNeto(self,retencion):
        sueldoActual = self.getSueldo()
        sueldoNeto = (sueldoActual * retencion)/100

        return sueldoNeto
    
    def __str__(self):
        return f"nombre {self.getNombre()} , sueldo {self.getSueldo()}"