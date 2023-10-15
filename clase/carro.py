from  vehiculo import Vehiculo

class Auto(Vehiculo):
   def __init__(self,kilometraje,marca,año,modelo,encendido):
        super().__init__(marca,año,modelo,encendido)
        self.kilometraje = kilometraje

        def __str__(self):
            return f"{self.kilometraje}"

carrito = Auto(2000,"marca","año","modelo",False)
    
print(carrito.__str__)



