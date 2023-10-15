from FiguraGeometrica import FiguraGeometrica


class Circulo(FiguraGeometrica):

    def __init__(self,radio:float,color_fondo: str,color_borde: str):
        super().__init__(color_borde,color_fondo)
        self.__radio = radio

    # metodos propios

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, nuevo_radio:float):
        self.__radio = nuevo_radio

    # metodos heredados

    def area(self):
        return 2*3,14*(self.radio * self.radio)
    def perimetro(self):
        return 3,14*self.radio
