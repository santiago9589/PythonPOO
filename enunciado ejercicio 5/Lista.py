# Crear una clase llamada ListaDeTareas con los siguientes atributos y métodos:
# • Atributo de instancia privado “lista_tareas” de tipo list. LISTO
# • Método de instancia público “agregarTarea(tarea)”, que recibe como argumento
# una tarea que debe ser agregada a la lista de tareas (atributo “lista_tareas”) y
# retorna el string “Tarea agregada correctamente a la lista” ó “La tarea no fue
# agregada a la lista” en caso que la tarea se haya agregado o no a la lista
# respectivamente.
# • Método de instancia público “quitarTarea(tarea)”, que recibe como argumento una
# tarea que debe ser eliminada de la lista de tareas (atributo “lista_tareas”) y retorna
# el string “Tarea eliminada correctamente de la lista” ó “La tarea no fue eliminada de
# la lista” en caso que la tarea se haya eliminado o no de la lista respectivamente.
# • Método de instancia público “mostrarTareas()”, que no recibe ningún argumento y
# retorna la lista de tareas (atributo “lista_tareas”) .
# Luego, se debe crear una instancia de ListaDeTareas, agregar tareas a la lista, eliminar
# tareas de la lista y finalmente imprimir la lista completa de tareas.
# Nota: el método “quitarTarea(tarea)” debe validar si la tarea a eliminar existe en la lista
# antes de ser eliminada.


class ListaDeTareas():
    def __init__(self):
        self.__lista_tareas = list()

    def  agregarTarea(self,nuevaTarea):
        if nuevaTarea != "" and  nuevaTarea not in self.getTareas():
                self.getTareas().append(nuevaTarea)
                return "Tarea agregada correctamente a la lista"
        else:
                return "La tarea no fue agregada a la lista"

    def  quitarTarea(self,nuevaTarea):
            if nuevaTarea in self.getTareas(): 
                self.getTareas().remove(nuevaTarea)
                return "Tarea eliminada correctamente de la lista"      
            else:
               return "La tarea no fue eliminada de la lista"
        
    def  mostrarTareas(self):
          return self.getTareas()
    
    def  getTareas(self):
          return self.__lista_tareas
    
    