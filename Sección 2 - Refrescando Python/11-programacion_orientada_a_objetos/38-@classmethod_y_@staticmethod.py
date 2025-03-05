"""
Existen tres tipos de métodos que puede tener una clase:
    - Métodos de instancia, que deben recibir una referencia a un objeto, a una instancia de clase,
    para ser utilizados, y estos métodos se suelen usar para trabajar con los objetos y/o sus atributos.
    - Métodos de clase, que deben recibir una referencia a la propia clase y además llevan @classmethod
    antes de su declaración, y se suelen usar como fábricas.
    - Métodos estáticos, que no reciben referencias, llevan @staticmethod antes de su declaración, son,
    efectivamente, funciones normales y corrientes creadas dentro de una clase.
"""


class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        # Se usa cls por convención, pero igual que con self, puede llamarse lo que quieras
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")


test = ClassTest()

# Todas estas son formas correctas de llamar a los distintos métodos
test.instance_method()
test.class_method()
test.static_method()
ClassTest.instance_method(test)
ClassTest.class_method()
ClassTest.static_method()
