# Ejercicio: Creación de una Clase para Gestionar Libros en una Biblioteca

# Supongamos que estás desarrollando un sistema de gestión de una biblioteca. Debes crear una clase llamada Libro que permita gestionar la información de los libros que se encuentran en la biblioteca. Cada libro debe tener los siguientes atributos:

# Título del libro
# Autor del libro
# Año de publicación
# Número de páginas
# La clase Libro debe tener métodos para:

# Inicializar un libro con los atributos mencionados.
# Mostrar la información del libro.
# Calcular el número de años que ha pasado desde su publicación.
# Permitir la actualización del número de páginas del libro.
# Además, debes crear una instancia de la clase Libro, inicializarla con algunos valores de ejemplo y luego realizar varias operaciones, como mostrar la información del libro, calcular cuántos años han pasado desde su publicación y actualizar el número de páginas.



class Libro:

    #atributo de clase

    codigo = 0

    def __init__(self,titulo,autor,añoPublic):
        self.__titulo = titulo
        self.__autor = autor
        self.__añoPublic = añoPublic
        Libro.codigo+=1

    @classmethod
    def getCodigo(cls):
        return cls.codigo

    @property
    def title(self):
        print("obteniendo titulo...")
        return self.__titulo
    
    @title.setter
    def title(self,nuevoTitle):
        print("modificando titulo")
        if(nuevoTitle == None):
            raise ValueError("hubo un error")
        self.__titulo = nuevoTitle

    @property
    def autor(self):
        print("obteniendo autor...")
        return self.__autor

    @autor.setter
    def autor(self,nuevoAutor:str):
        print("modificando Autor")
        if(nuevoAutor.isdigit):
            raise ValueError("hubo un error")
        self.__autor= nuevoAutor
        
    @property
    def añoPublic(self):
        print("obteniendo Año de Publicion...")
        return self.__añoPublic

    @añoPublic.setter
    def añoPublic(self,nuevoAñoPublic):
        print("modificando Año de Publicion")
        if(nuevoAñoPublic == None):
            raise ValueError("hubo un error")
        self.__añoPublic= nuevoAñoPublic
    def __str__(self):
        return f"el libro {self.title} de {self.autor} en el año {self.añoPublic} y el numero {self.getCodigo()}  de la editorial"