from typing import List

"""
En Python, podemos especificar qué tipo de valores se espera
que reciba y/o retorne una función usando anotaciones de tipo.
"""


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


print(list_avg([1, 2, 3, 4]))

# A continuación algunos ejemplos de uso


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count


class BookShelf:
    """
    Para usar empaquetado y anotaciones:
    def __init__(self, *books: Book):
    Se pone el tipo de los elementos individuales, no el del empaquetado, como podría ser Tuple[Book]
    """

    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book '{self.name}', '{self.book_type}', weighting {self.weight}g>"

    @classmethod
    # Si no existiera la clase Book más arriba, esto es lo que hay que hacer para que el método pueda devolver un objeto de la misma clase a la que pertenece
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)
