# Todos los métodos con dos barras bajas a los lados son métodos
# mágicos, y se ejecutan automáticamente bajo ciertas circunstancias.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old."
        # El método __str__ es como hacer en Java:
        # @Override
        # public string toString(){}
        # Se usa para imprimir el objeto de cara a los usuarios del programa.

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"
        # __repr__ es similar a __str__, pero generalmente está dirigido a los
        # programadores trabajando con el programa.


bob = Person("Bob", 35)
print(bob)  # Si no tuvieramos ni un método str ni uno repr, imprimiría algo
# por el estilo de <__main__.Person object at 0x************>
# Si tuvieramos un repr pero no un str, imprimiría el repr por defecto

# También se pueden llamar manualmente, como cualquier otro método
print(bob.__str__())
print(bob.__repr__())
