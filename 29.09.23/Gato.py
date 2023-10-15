from animal import Animal


class Gato(Animal):

    def __init__(self,nombre):
        self.nombre = nombre


    def hacerSonido(self):
        return f"hola soy un gato llamado {self.nombre}"
    
    def __str__(self):
        return f"soy {self.nombre}"



