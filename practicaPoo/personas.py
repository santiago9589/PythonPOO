from abc import ABC


class Persona(ABC):
   def __init__(self,dni,nombre,edad,estado):
      self.__dni = dni
      self.__nombre = nombre
      self.__edad = edad
      self.__estado = estado
   
   
   def getDni(self):
      return self.__dni
    
   def setDni(self,nuevoDni):
      self.__dni = nuevoDni
      
   def getNombre(self):
      return self.__nombre
    
   def setNombre(self,nuevoNombre):
      self.__nombre = nuevoNombre

   def getEdad(self):
      return self.__edad
    
   def setEdad(self,nuevaEdad):
      self.__edad = nuevaEdad

   def getEstado(self):
      return self.__estado
    
   def setEstado(self,nuevaEstado):
      self.__estado = nuevaEstado