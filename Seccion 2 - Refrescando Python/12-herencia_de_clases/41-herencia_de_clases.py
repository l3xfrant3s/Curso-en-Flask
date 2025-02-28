class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
        # !r llama al método repr de aquello que pongas al lado, en este caso lo hará de self.name, poniendo las comillas automáticamente

    def disconnect(self):
        self.connected = False
        print("Disconnected.")


# Al heredar de la clase Device, sus métodos también son accesibles desde Printer, sin tener que declararlos explícitamente.
# Para usar los métodos de la clase heredada, hay que referenciar la clase heredada con super().
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(
            name, connected_by
        )  # Llamamos al construcctor de la clase de la que hereda
        self.capacity = capacity
        self.remaining_pages = capacity
        # Seguimos pudiendo añadir nuestras propias propiedades a la clase

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages}/{self.capacity} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


"""
Hay cierta jerarquía con las llamadas a métodos de una clase:
    - Primero se comprueba si el método está definido en la propia clase.
    - Luego si está definido en cualquier clase de la que herede.
    - Por último si está definido en la clase Object (pues todas las clases heredan de Object)
"""

printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnect()
printer.print(20)
