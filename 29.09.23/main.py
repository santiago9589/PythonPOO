from Perro import Perro
from Gato import Gato
from Pajaro import Pajaro


nuevoPajaro = Pajaro("JAIME")
nuevoPerro = Perro("JUAN")
nuevoGato = Gato("MIMI")

print(nuevoPajaro.hacerSonido())
print(nuevoPerro.hacerSonido())
print(nuevoGato.hacerSonido())

print(nuevoPajaro.volar())
