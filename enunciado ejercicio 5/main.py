from Lista import ListaDeTareas


nuevaLista = ListaDeTareas()

print(nuevaLista.mostrarTareas()) # muestro lista

print(nuevaLista.agregarTarea("limpiar los platos")) # agrego a la lista
print(nuevaLista.agregarTarea("pasear al perro"))  # agrego a la lista

print(nuevaLista.mostrarTareas()) # muestro lista

print(nuevaLista.quitarTarea("limpiar los platos")) # quito de  la lista

print(nuevaLista.mostrarTareas()) # muestro lista

print(nuevaLista.agregarTarea("")) # agrego elemento vacio para que de error
print(nuevaLista.quitarTarea("manejar a la tienda")) # elimino elemento que no existe  para que de error
print(nuevaLista.agregarTarea("pasear al perro")) # agrego elemento vacio para que de error

print(nuevaLista.mostrarTareas()) # muestro lista