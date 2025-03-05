"""
No siempre tiene sentido usar herencia, y de hecho, no se usa mucho en Python.
"""


class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"BookShelf with {self.quantity} books."


shelf = BookShelf(300)
print(shelf)


# Como se puede ver, Book no usa ninguna propiedad o método de BookShelf
class Book(BookShelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"Book {self.name}."


book = Book("Harry Potter", 120)
print(book)


"""
El problema aquí está en la relación entre un libro y una estantería.
Un libro no es una Poke-evolución de una estantería, no añade ni usa
funcionalidad alguna de una estantería, en ese sentido no tienen nada que ver.
En lo que sí están relacionandos es que una estantería puede contener muchos libros.

En estos casos se usa la composición de clases.
"""


class BookShelf:
    # En este caso, BookShelf contiene un empaquetado de libros, haciendo de composición de clases
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    # De Book eliminamos la herencia a BookShelf, pues nunca fue necesaria
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}."


book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)

print(shelf)
print(book)
print(book2)
