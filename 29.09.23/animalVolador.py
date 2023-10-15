from abc import ABC, abstractclassmethod

class AnimalVolador(ABC):
    
    @abstractclassmethod
    def volar():
        pass