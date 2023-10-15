from libro import Libro


libros = list()
autores = ["pedro","maria","jose"]
libro = ["maryryr","anastaisa","jazmin"]

for i in range(3):

    libroCreado = Libro(libro[i],autores[i],2000)
    libros.append(libroCreado)
    print(libroCreado.getCodigo())

