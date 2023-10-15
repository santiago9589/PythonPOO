class Persona():

    def __init__(self):
        self

    def __init__(self, nombre=" ", edad=0, sexo="HOMBRE"):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = self.generarDni()
        self.__sexo = sexo
        self.__altura = 0
        self.__peso = 0

    def __init__(self, nombre=" ", edad=0, sexo="HOMBRE", altura=0, peso=0):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = self.generarDni()
        self.__sexo = sexo
        self.__altura = altura
        self.__peso = peso

    def generarDni(self):
        return 4678

    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__DNI
    
    def getEdad(self):
        return self.__edad
    
    def getSexo(self):
        return self.__sexo
    def getPeso(self):
        return self.__peso
    
    def getAltura(self):
        return self.__altura
    
    def getAltura(self):
        return self.__peso
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setEdad(self,edad):
        self.__edad = edad
    def setAltura(self,altura):
        self.__altura = altura
    def setSexo(self,sexo):
        self.__sexo = sexo
    def setPeso(self,peso):
        self.__peso = peso
    
    def __str__(self):
        return f"nombre : {self.getNombre()} peso: {self.getPeso()}"
   