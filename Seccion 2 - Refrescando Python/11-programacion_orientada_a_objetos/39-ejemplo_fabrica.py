class Book:
    TYPES = ("hardcover", "paperback")
    # Esta propiedad es de clase, eso significa que no tienes que crear un objecto para acceder a ella

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book '{self.name}', '{self.book_type}', weighting {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
        # También es posible hacer esto, aunque se recomienda encarecidamente usar cls
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)
        # También es posible hacer esto, aunque se recomienda encarecidamente usar cls
        return Book(name, Book.TYPES[1], page_weight)


book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print(book)
print(light)
