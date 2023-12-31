# La clase Cliente debe contener:
# • Atributos de instancia:
# o razon_social de tipo string.
# o cuit de tipo string.
# o tipo_persona de tipo string (física o jurídica).
# o domicilio de tipo string.
# o cuentas_bancarias de tipo list.
# • Método constructor:
# o __init__(self, *args) para inicializar los atributos de instancia razon_social, cuit,
# tipo_persona y domicilio con los valores recibidos como parámetros, y el atributo
# cuentas_bancarias como una nueva lista.
# • Métodos de instancia:
# o crear_nueva_cuenta_bancaria (), que retorna un booleano indicando si la operación se
# realizó correctamente. Para crear una nueva instancia de CuentaBancaria se debe indicar
# el tipo de cuenta (CajaDeAhorro o CuentaCorriente) e ingresar nro_cuenta, alias, cbu, saldo
# y demás valores necesarios según el tipo de cuenta. El nuevo objeto CuentaBancaria debe
# agregarse a la lista cuentas_bancarias.

from CajaDeAhorro import CajaDeAhorro
from CuentaCorriente import CuentaCorriente
from CuentaBancaria import CuentaBancaria


class Cliente():

    __idCuenta = 0

    def __init__(self, razon_social, cuit, tipo_persona, domicilio):
        self.__razon_social = razon_social
        self.__cuit = cuit
        self.__tipo_persona = tipo_persona
        self.__domicilio = domicilio
        self.__cuentas_bancarias = list[CuentaBancaria]()
        self.__idCuenta += self.__idCuenta

    def crear_nueva_cuenta_bancaria(self, Cuenta: CuentaBancaria):
    
            if (Cuenta != None):
                self.cuentas_bancarias.append({
                    "numero" : Cuenta.nro_cuenta,
                    "cuenta": Cuenta
                })
                return True
            else:
                return False
    
    @property
    def razon_social(self):
        return self.__razon_social

    @razon_social.setter
    def razon_social(self, nuevaRazon_social):
        self.__razon_social = nuevaRazon_social

    @property
    def cuit(self):
        return self.__cuit

    @cuit.setter
    def cuit(self, nuevacuit):
        self.__cuit = nuevacuit

    @property
    def tipo_persona(self):
        return self.__tipo_persona

    @tipo_persona.setter
    def tipo_persona(self, nuevatipo_persona):
        self.__tipo_persona = nuevatipo_persona

        
    @property
    def domicilio(self):
        return self.__domicilio

    @domicilio.setter
    def domicilio(self, nuevadomicilio):
        self.__domicilio = nuevadomicilio

    @property
    def cuentas_bancarias(self):
        return self.__cuentas_bancarias
    
    def obtenerCuenta(self,numero):
        cuentaEncontrada = None
        for cuentas in self.cuentas_bancarias:
            if cuentas.get("numero") == numero:          
                cuentaEncontrada:CajaDeAhorro | CuentaCorriente = cuentas.get("cuenta")
                break
        return cuentaEncontrada
