# Esta función puede ser redefinida como una función lambda
def add(x, y):
    return x + y


# Crearla y no asignarla a nada hace que no la puedas usar
lambda x, y: x + y

# Podemos asignarla a una variable, lo cual permitirá usarla como si fuera una función
add = lambda x, y: x + y
print(add(5, 7))

# O podemos usarla in situ

print((lambda x, y: x + y)(5, 7))


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
# Alternativamente para la comprensión de la lista de arriba, se puede usar la función map()
doubled = map(double, sequence)

# Ambas pueden ser reescritas usando una función lambda,
# ahorrandonos tener que declarar una función más arriba,
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled = map(lambda x: x * 2, sequence)
