from abc import ABC, abstractclassmethod

class Animal(ABC):
    
    @abstractclassmethod
    def hacerSonido():
        pass