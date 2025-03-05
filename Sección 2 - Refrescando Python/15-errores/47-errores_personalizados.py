"""
Para crear un error personalizado, todo lo que hay que hacer es crear una clase que herede de Exception u otra clase de error, como ValueError.
Aunque existe la posibilidad, no es necesario crear nada más dentro de la clase, pues su propósito principal es ser más descriptivo cuando salte el error.
"""


class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages"
            )

        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}")


python101 = Book("Python101", 50)
try:
    python101.read(35)
    python101.read(50)
except TooManyPagesReadError as tmpre:
    print(tmpre)
