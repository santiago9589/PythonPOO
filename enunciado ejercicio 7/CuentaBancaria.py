#  La clase CuentaBancaria, debe contener:
# • Atributos de instancia:
# o nro_cuenta de tipo string.
# o cbu de tipo string.
# o alias de tipo string.
# o saldo de tipo float.
# o movimientos de tipo list.
# • Método constructor:
# o __init__ (self, *args) para inicializar los atributos de instancia nro_cuenta, cbu, alias y saldo
# con los valores recibidos como parámetros; y el atributo movimientos como una nueva
# lista.
# • Métodos de instancia:
# o consultar_saldo (), que retorna el saldo de la cuenta.
# o depositar (monto_a_depositar de tipo float), que retorna un booleano indicando si la
# operación se realizó correctamente o no. En caso que el depósito se haya realizado
# correctamente, y luego de haber actualizado el saldo, debe agregar un nuevo elemento a
# la lista movimientos, donde elemento será una tupla que tendrá los siguientes elementos:
# fecha de tipo date, “depósito”, monto depositado y saldo.
# • Métodos abstractos:
# o extraer (monto_a_extraer de tipo float), que retorna un valor booleano. En caso que la
# extracción se haya realizado correctamente, y luego de haber actualizado el saldo, debe
# agregar un nuevo elemento a la lista movimientos, donde elemento será una tupla que
# tendrá los siguientes elementos: fecha de tipo date, “extracción”, monto extraído y saldo.
# o transferir (monto_a_transferir de tipo float, cuenta_destino de tipo CuentaBancaria), que
# retorna un valor booleano. En caso que la transferencia se haya realizado correctamente,
# y luego de haber actualizado el saldo, debe agregar un nuevo elemento a la lista
# movimientos, donde elemento será una tupla que tendrá los siguientes elementos: fecha
# de tipo date, “transferencia”, monto transferido y saldo.

from datetime import datetime
from abc import abstractclassmethod


class CuentaBancaria():
    def __init__(self, nro_cuenta, cbu, alias, saldo):
        self.__nro_cuenta = nro_cuenta
        self.__cbu = cbu
        self.__alias = alias
        self.__saldo = saldo
        self.__movimientos= list()

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, monto_a_depositar):
        if (monto_a_depositar > 0):
            self.saldo += monto_a_depositar

            self.movimientos.append((
                datetime.now(),
                "Deposito",
                monto_a_depositar,
                self.saldo
            ))
            return True
        else:
            return False
        
    
    def registarMovimiento(self, fecha, actividad: str, montoOperado, saldoFinal):
        self.movimientos.append((
            datetime.now(),
            actividad,
            montoOperado,
            saldoFinal
        ))

    @abstractclassmethod
    def extraer(self, monto_a_extraer):
        pass

    @abstractclassmethod
    def transferir(self, monto_a_transferir, cuenta_destino):
        pass

    @property
    def nro_cuenta(self):
        return self.__nro_cuenta

    @nro_cuenta.setter
    def nro_cuenta(self, nuevanro_cuenta):
        self.__nro_cuenta = nuevanro_cuenta

    @property
    def cbu(self):
        return self.__cbu

    @cbu.setter
    def cbu(self, nuevacbu):
        self.__cbu = nuevacbu

    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, nuevaalias):
        self.__alias = nuevaalias

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevasaldo):
        self.__saldo = nuevasaldo

    @property
    def movimientos(self):
        return self.__movimientos
