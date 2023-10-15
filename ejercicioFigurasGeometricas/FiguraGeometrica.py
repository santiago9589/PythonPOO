from abc import ABC

class FiguraGeometrica(ABC):
 

    def __init__(self,color_fondo: str,color_borde: str):
        self.__color_fondo = color_fondo
        self.__color_borde = color_borde

     # metodos propios

    @property
    def color_fondo(self):
        return self.__color_fondo

    @color_fondo.setter
    def color_fondo(self, nuevo_color_fondo:float):
        self.__color_fondo = nuevo_color_fondo

    @property
    def color_borde(self):
        return self.__color_borde

    @color_borde.setter
    def color_borde(self, nuevo_color_borde:float):
        self.__color_borde = nuevo_color_borde

    # metodos abstractos

    def area(self):
        pass
    def perimetro(self):
        pass
        