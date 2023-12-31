# Ejercicio cuentas bancarias – clases y métodos abstactos

# Desarrollar en Python un software que implemente un modelo de gestión bancaria de acuerdo a
# los siguientes requerimientos:


# Se debe crear una clase abstracta llamada CuentaBancaria, una clase CajaDeAhorro y una clase
# CuentaCorriente, ambas que hereden de CuentaBancaria. Una clase Cliente que entre sus
# atributos tenga una lista de elementos de tipo CuentaBancaria, y una clase Banco que entre sus
# atributos tenga una lista de elementos de tipo Cliente.


# La clase CuentaBancaria, debe contener:
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


# La clase Banco debe contener:
# • Atributos de instancia:
# o nombre de tipo string.
# o domicilio de tipo string.
# o clientes de tipo list.
# • Método constructor:
# o __init__(self, *args) para inicializar los atributos de instancia nombre y domicilio con los
# valores recibidos como parámetros, y el atributo clientes como una nueva lista.
# • Métodos de instancia:
# o crear_nuevo_cliente (), que retorna un booleano indicando si la operación se realizó
# correctamente. Para crear una nueva instancia de Cliente se debe ingresar razon_social,
# cuit, tipo_persona y domicilio. El nuevo objeto Cliente debe agregarse a la lista clientes.
# Para validar el modelo de gestión bancaria implementado, incluya una función main() con las
# instrucciones necesarias para crear un objeto Banco, tres instancias de Clientes (como mínimo)
# cada uno de ellos con dos objetos CuentaBancaria (como mínimo), uno de tipo CajaDeAhorro y
# otro de tipo CuentaCorriente.
# Luego simule varias operaciones de depósito, extracción y transferencias entre las cuentas.
# Finalmente, muestre por pantalla los datos de los clientes del banco, con los saldos de sus cuentas
# y el registro de los movimientos de las mismas.
# Nota:
# Todos los atributos de instancia declarados en las clases deberán ser privados y accesibles
# mediante propiedades públicas de tipo getters y setters (usando el decorador @property).
# Para trabajar con fechas debe importar el módulo datetime.

from Banco import Banco
from Cliente import Cliente
from CajaDeAhorro import CajaDeAhorro
from CuentaCorriente import CuentaCorriente

# creacion del banco

nuevoBanco = Banco("Santander Rio", "Av paseo colon 2045")

cliente1 = Cliente("panaderia", 29045, "fisica", "Av san juan 4056")
nuevaCuenta1 = CajaDeAhorro(1,1,"cuenta1",2000,3000,3000,5,5)
nuevaCuenta2 = CuentaCorriente(2,2,"cuenta2",2000,5)
cliente1.crear_nueva_cuenta_bancaria(nuevaCuenta1)
cliente1.crear_nueva_cuenta_bancaria(nuevaCuenta2)

cliente2 = Cliente("kiosko", 29045, "fisica", "Av hipolito 203")
nuevaCuenta3 = CajaDeAhorro(3,3,"cuenta3",2000,3000,3000,5,5)
nuevaCuenta4 = CuentaCorriente(4,4,"cuenta4",2000,5)
cliente2.crear_nueva_cuenta_bancaria(nuevaCuenta3)
cliente2.crear_nueva_cuenta_bancaria(nuevaCuenta4)

cliente3 = Cliente("lavadora", 33455, "fisica", "Av tutvg 344")
nuevaCuenta5 = CajaDeAhorro(3,3,"cuenta3",2000,3000,3000,5,5)
nuevaCuenta6 = CuentaCorriente(4,4,"cuenta4",2000,5)
cliente3.crear_nueva_cuenta_bancaria(nuevaCuenta5)
cliente3.crear_nueva_cuenta_bancaria(nuevaCuenta6)

nuevoBanco.crear_nuevo_cliente(cliente1)
nuevoBanco.crear_nuevo_cliente(cliente2)
nuevoBanco.crear_nuevo_cliente(cliente3)


# deposito

cuentaEjemplo1 = cliente1.obtenerCuenta(1)
cuentaEjemplo2 = cliente2.obtenerCuenta(3)

if cuentaEjemplo1 != None and cuentaEjemplo2 != None:
    
    cuentaEjemplo1.depositar(200.56)
    print(cuentaEjemplo1.consultar_saldo())

# extraccion

    cuentaEjemplo1.extraer(100.00)
    print(cuentaEjemplo1.consultar_saldo())

# transferencia

    cuentaEjemplo1.transferir(100.00,cuentaEjemplo2)
    print(cuentaEjemplo1.consultar_saldo())

#informacion de clientes y movimientos

listaDeClientes = nuevoBanco.clientes

for Clientes in listaDeClientes:
    for cuentas in Clientes.cuentas_bancarias:
        print(cuentas.get("cuenta").consultar_saldo())
        print(cuentas.get("cuenta").movimientos)