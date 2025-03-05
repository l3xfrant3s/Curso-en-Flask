"""
This coding exercise requires you to complete an implementation of three methods of a class:
    The __init__  method, which should take an argument, name . It should initialise self.name  to be the argument, and self.items  to be an empty list.
    The add_item  method, which should append a dictionary representing an item to the store's items  property. The dictionary should have keys name  and price .
    The stock_price  method, which should add up each item price inside self.items  to come up with a total, and return that.
"""


class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        """# Una solución propuesta por el instructor:
        total = 0
        for item in self.items:
            total += item["price"]
        return total
        """
        # La otra es lo que yo hice
        return sum([item["price"] for item in self.items])


tienda = Store("Megasaurio")

tienda.add_item("Pan", 100)
tienda.add_item("Más pan", 200)

print(tienda.stock_price())
