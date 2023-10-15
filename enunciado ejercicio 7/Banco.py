# La clase Banco debe contener:
# • Atributos de instancia:
# odomicilio de tipo string.
# o domicilio de tipo string.
# o clientes de tipo list.
# • Método constructor:
# o __init__(self, *args) para inicializar los atributos de instanciadomicilio y domicilio con los
# valores recibidos como parámetros, y el atributo clientes como una nueva lista.
# • Métodos de instancia:
# o crear_nuevo_cliente (), que retorna un booleano indicando si la operación se realizó
# correctamente. Para crear una nueva instancia de Cliente se debe ingresar razon_social,
# cuit, tipo_persona y domicilio. El nuevo objeto Cliente debe agregarse a la lista clientes.
#

from Cliente import Cliente


class Banco():
    def __init__(self, nombre, domicilio):
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__clientes = list[Cliente]()

    def crear_nuevo_cliente(self, nuevoCliente:Cliente):
        if (nuevoCliente != None):
            self.clientes.append(nuevoCliente)
            return True
        else:
            return False

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    @property
    def domicilio(self):
        return self.__domicilio

    @domicilio.setter
    def domicilio(self, nuevoDomicilio):
        self.__domicilio = nuevoDomicilio

    @property
    def clientes(self):
        return self.__clientes
