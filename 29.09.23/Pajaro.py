from animal import Animal
from animalVolador import AnimalVolador


class Pajaro(Animal,AnimalVolador):

    def __init__(self,nombre):
        self.nombre = nombre

    def hacerSonido(self):
        return f"hola soy un pajaro llamado {self.nombre}"
    
    def volar(self):
        return f"Mira como vuelo obvio soy un ave"
    
    def __str__(self):
        return f"soy {self.nombre}"


