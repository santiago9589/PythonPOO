from animal import Animal


class Perro(Animal):

    def __init__(self,nombre):
        self.nombre = nombre


    def hacerSonido(self):
        return f"hola soy un perro llamado {self.nombre}"
    
    def __str__(self):
        return f"soy {self.nombre}"




