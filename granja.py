# Clase Animal
class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.peso = 0

    def alimentar(self):
        print(f"{self.tipo} {self.nombre} ha sido alimentado.")

    def vacunar(self):
        print(f"{self.tipo} {self.nombre} ha sido vacunado.")

    def registrar_peso(self, peso):
        self.peso = peso
        print(f"Peso de {self.tipo} {self.nombre} registrado: {self.peso} kg")

    def __str__(self):
        return f"{self.tipo} llamado {self.nombre}"


class Corral:
    def __init__(self, id_corral):
        self.id_corral = id_corral
        self.animales = []

    def asignar_animal(self, animal):
        self.animales.append(animal)
        print(f"{animal} asignado al corral {self.id_corral}.")

    def quitar_animal(self, animal):
        if animal in self.animales:
            self.animales.remove(animal)
            print(f"{animal} retirado del corral {self.id_corral}.")

    def limpiar(self):
        print(f"Corral {self.id_corral} ha sido limpiado.")

    def listar_animales(self):
        print(f"Corral {self.id_corral} contiene:")
        for animal in self.animales:
            print(f" - {animal}")


class Empleado:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def realizar_tarea(self, tarea):
        print(f"{self.nombre} está realizando la tarea: {tarea}")

    def registrar_asistencia(self):
        print(f"Asistencia registrada para {self.nombre} ({self.rol})")

    def reportar_incidencias(self, incidencia):
        print(f"{self.nombre} ha reportado: {incidencia}")


class Granja:
    def __init__(self, nombre):
        self.nombre = nombre
        self.corrales = []
        self.empleados = []

    def agregar_corral(self, corral):
        self.corrales.append(corral)
        print(f"Corral {corral.id_corral} agregado a la granja.")

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} contratado para la granja.")

    def cerrar(self):
        print("Cerrando la granja. Todos los empleados dejan de estar vinculados.")
        self.empleados.clear()


if __name__ == "__main__":
   
    granja = Granja("El Buen Pastor")

    
    emp1 = Empleado("Carlos", "Alimentación")
    emp2 = Empleado("Laura", "Vigilancia")
    granja.contratar_empleado(emp1)
    granja.contratar_empleado(emp2)

    
    emp1.registrar_asistencia()
    emp1.realizar_tarea("Alimentar animales")
    emp1.reportar_incidencias("Gallina enferma")

   
    corral1 = Corral(1)
    corral2 = Corral(2)
    granja.agregar_corral(corral1)
    granja.agregar_corral(corral2)

   
    vaca = Animal("Lola", "Vaca")
    cerdo = Animal("Porky", "Cerdo")
    gallina = Animal("Pepita", "Gallina")

    
    corral1.asignar_animal(vaca)
    corral1.asignar_animal(cerdo)
    corral2.asignar_animal(gallina)

    vaca.alimentar()
    vaca.vacunar()
    vaca.registrar_peso(250)

    
    corral1.limpiar()

   
    corral1.listar_animales()
    corral2.listar_animales()

    
    granja.cerrar()