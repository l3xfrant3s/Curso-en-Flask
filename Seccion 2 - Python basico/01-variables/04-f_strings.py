name = "Bob"
greeting = "Hello, Bob"
print(greeting)  # Va a imprimir "Hello, Bob"

name = "Rolf"
print(greeting)  # Va a imprimir "Hello, Bob" otra vez

greeting = f"Hello, {name}"  # Va a guardar "Hello, " y lo que quiera que haya en name,
# en este caso Rolf

print(greeting)  # Va a imprimir "Hello, Rolf"

name = "Alexis"  # Modificar name ahora no va a cambiar greeting
print(greeting)  # Va a imprimir "Hello, Rolf" otra vez

# Usando directamente la f-string, modificar name más arriba va a modificar lo que se imprime
print(
    f"Hello, {name}"
)  # Va a imprimir "Hello, " y lo que tenga name, este caso "Alexis"

name = "estudiante de DAM"
print(
    f"Hola {name}"
)  # Va a imprimir "Hola " y lo que tenga name, este caso "Estudiante de DAM"
