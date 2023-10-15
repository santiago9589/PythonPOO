class Vehiculo():
    def __init__(self,marca,año,modelo,encendido):
        self.marca =marca
        self.año =año
        self.modelo =modelo
        self.encendido =encendido
    def encender(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False



carro = Vehiculo("marca","año","modelo",False)



