# La clase CajaDeAhorro debe contener:
# • Atributos de instancia:
# o monto_limite_extracciones de tipo float.
# o monto_limite_transferencias de tipo float.
# o cant_extracciones_disponibles de tipo int.
# o cant_transferencias_disponibles de tipo int.
# • Método constructor:
# o __init__(self, args *) para inicializar los atributos de instancia nro_cuenta, alias, cbu, saldo,
# monto_limite_extracciones, monto_limite_transferencias, cant_extracciones_disponibles
# y cant_transferencias_disponibles con los valores recibidos como parámetros.
# • Métodos de instancia:
# o extraer (monto_a_extraer de tipo float), que retorna un booleano indicando si la operación
# se realizó correctamente o no. La extracción se considerará como correcta si
# monto_a_extraer es mayor a cero, si monto_a_extraer no es superior al saldo, si
# monto_a_extraer no es superior al monto_limite_extracciones y si la
# cant_extracciones_disponibles es mayor a cero, en cuyo caso se deberá actualizar el saldo
# y cant_extracciones_disponibles; e invocar al método heredado para registrar el
# movimiento.
# o transferir (monto_a_transferir de tipo float, cuenta_destino de tipo CuentaBancaria), que
# retorna un booleano indicando si la operación se realizó correctamente o no. La
# transferencia se considerará como correcta si monto_a_transferir es mayor a cero, si
# monto_a_transferir no es superior al saldo, si monto_a_transferir no es superior al
# monto_limite_transferencias y si la cant_transferencias_disponibles es mayor a cero, en
# cuyo caso se deberá actualizar el saldo y cant_transferencias_disponibles de la cuenta
# origen y el saldo de la cuenta destino; e invocar al método heredado para registrar el
# movimiento.

from CuentaBancaria import CuentaBancaria
from datetime import datetime


class CajaDeAhorro(CuentaBancaria):
    def __init__(self, nro_cuenta, cbu, alias, saldo, monto_limite_extracciones, monto_limite_transferencias, cant_extracciones_disponibles, cant_transferencias_disponibles):
        super().__init__(nro_cuenta, cbu, alias, saldo)
        self.monto_limite_extracciones = monto_limite_extracciones
        self.monto_limite_transferencias = monto_limite_transferencias
        self.cant_extracciones_disponibles = cant_extracciones_disponibles
        self.cant_transferencias_disponibles = cant_transferencias_disponibles

    def extraer(self, monto_a_extraer):

        if (monto_a_extraer > 0 and self.saldo > monto_a_extraer and self.monto_limite_extracciones > monto_a_extraer and self.cant_extracciones_disponibles > 0):

            self.saldo -= monto_a_extraer
            self.cant_extracciones_disponibles -= 1
            self.registarMovimiento( datetime.now(),"Extraccion",monto_a_extraer,self.saldo)
            return True
        else:
            return False

    def transferir(self, monto_a_transferir, cuenta_destino: CuentaBancaria):
        if (monto_a_transferir > 0 and self.saldo > monto_a_transferir and self.monto_limite_transferencias > monto_a_transferir and self.cant_transferencias_disponibles > 0):
            self.saldo -=monto_a_transferir
            self.cant_transferencias_disponibles -= 1
            cuenta_destino.saldo += monto_a_transferir
            self.registarMovimiento( datetime.now(),
                "Transferencia",
                monto_a_transferir,
                self.saldo)
            return True
        else:
            return False
