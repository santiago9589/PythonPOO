from Empleado import Empleado



class Programador(Empleado):
    def __init__(self,nombre,apellido):
        super().__init__(nombre,apellido)

    def calcular_salario(self):
        print(f"el sueldo de un progamador es {self.sueldoBase * 1,25}")