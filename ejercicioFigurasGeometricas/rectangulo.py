from FiguraGeometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica):


    def __init__(self,base:float,altura:float,color_fondo: str,color_borde: str):
        super().__init__(color_borde,color_fondo)
        self.__base = base
        self.__altura = altura

    # metodos propios

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, nuevo_base:float):
        self.__base = nuevo_base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, nuevo_altura:float):
        self.__altura = nuevo_altura

    # metodos heredados

    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return self.base + self.altura
