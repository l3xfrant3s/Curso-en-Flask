a = 25
b = a  # b = 25

print(a)
print(b)  # ambos imprimen 25, al hacer referencia al mismo valor

b = 17  # modificar b no va a modificar a

print(a)  # a sigue haciendo referencia al mismo valor que antes mientras que b hace
print(b)  # referencia a un valor distinto, por lo que van a imprimir valores distintos
