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

