# La clase CuentaCorriente debe contener:
# • Atributos de instancia:
# o monto_maximo_descubierto de tipo float.
# • Método constructor:
# o __init__(self, *args) para inicializar los atributos de instancia nro_cuenta, alias, cbu, saldo
# y monto_maximo_descubierto con los valores recibidos como parámetros.
# • Métodos de instancia:
# o extraer (monto_a_extraer de tipo float), que retorna un booleano indicando si la operación
# se realizó correctamente o no. La extracción se considerará como correcta si
# monto_a_extraer es mayor a cero, si monto_a_extraer no es superior al saldo más el
# monto_maximo_descubierto, en cuyo caso se deberá actualizar el saldo; e invocar al
# método heredado para registrar el movimiento.
# o transferir (monto_a_transferir de tipo float, cuenta_destino de tipo CuentaBancaria), que
# retorna un booleano indicando si la operación se realizó correctamente o no. La
# transferencia se considerará como correcta si monto_a_transferir es mayor a cero, si
# monto_a_transferir no es superior al saldo más el monto_maximo_descubierto, en cuyo
# caso se deberá actualizar el saldo de la cuenta origen y el saldo de la cuenta destino; e
# invocar al método heredado para registrar el movimiento.

from CuentaBancaria import CuentaBancaria
from datetime import datetime


class CuentaCorriente(CuentaBancaria):
    def __init__(self, nro_cuenta, cbu, alias, saldo, monto_maximo_descubierto):
        super().__init__(nro_cuenta, cbu, alias, saldo)
        self.monto_maximo_descubierto = monto_maximo_descubierto
      

    def extraer(self, monto_a_extraer):
        if (monto_a_extraer > 0 and (self.saldo+self.monto_maximo_descubierto) > monto_a_extraer):
            self.saldo -= monto_a_extraer
            self.registarMovimiento(
                datetime.now(),
                "Extraccion",
                monto_a_extraer,
                self.saldo
            )
            return True
        else:
            return False

    def transferir(self, monto_a_transferir, cuenta_destino: CuentaBancaria):
        if (monto_a_transferir > 0 and (self.saldo+self.monto_maximo_descubierto) > monto_a_transferir):
            self.saldo -= monto_a_transferir
            cuenta_destino.saldo += monto_a_transferir
            self.registarMovimiento(
                datetime.now(),
                "Transferencia",
                monto_a_transferir,
                self.saldo
            )
            return True
        else:
            return False
