from Empleado import Empleado



class Gerente(Empleado):
    def __init__(self,nombre,apellido):
        super().__init__(nombre,apellido)

    def calcular_salario(self):
        print(f"el sueldo de un gerente es {self.sueldoBase * 2}")

    def probarUnaExcepcion(self,num,num2):
        try:
            resultado = num/num2
        except Exception as e:
            print("NO SE PUEDEEEEEEEEEEEEEEE")
        else:
            print("biennnnn")