# Así es como se declara una clase en Python, el método __init__ es el que inicializa los objetos y se ejecuta al llamar a la clase.
# self es una referecia al propio objeto, igual que this en Java, por ejemplo, pero en Python se puede llamar lo que quieras.
# Cualquier método de clase que crees debe tener, al menos, un parámetro para el objeto sobre el que va a trabajar.
# Los métodos de clase son como cualquier otra función, así que pueden tomar tantos argumentos como crean conveniente


class Student:
    def __init__(self, name, grades):
        self.name = name  # Así se definen las propiedades de la clase
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student1 = Student("Rolf", (90, 90, 93, 78, 90))
student2 = Student("Bob", (100, 100, 93, 78, 90))
print(student1.name)  # Imprime "Rolf"
print(student1.grades)  # Imprime "(90, 90, 93, 78, 90)"
# Ambos dan el resultado igual de bien, aunque es preferible usar la forma de abajo
print(Student.average_grade(student1))
print(student1.average_grade())
