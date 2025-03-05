from typing import List, Optional


class Student:
    # Usar valores mutables como valores por defecto es una muy mala idea
    # porque se crea en memoria cuando se define la clase, no cuando se crea el objeto.
    def __init__(self, name: str, grades: List[int] = []):
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)  # Solo Bob hizo el examen
# Pero ambos tienen la misma nota
print(bob.grades)  # Ambas van a imprimir [90]
print(rolf.grades)


# Esto se puede arreglar así


class Student:
    # Poniendo por defecto None, sigue siendo un parámetro opcional
    # Podemos importar Optional para que le quede más claro al código
    # que es opcional y va a recibir un valor más adelante
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []  # Si grades es None, entonces creará una lista vacia

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)  # Solo Bob hizo el examen
print(bob.grades)  # Aquí imprime [90]
print(rolf.grades)  # Y aquí []
