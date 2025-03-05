"""
En Python, hay que hacer un distinción importante entre nombres de variables y valores de variables.
Teniendo que x = 0, no es correcto decir que una variable x *es* 0, si no que el nombre de variable x tiene asignado el valor 0
"""

# Aquí no es correcto decir que creamos una lista vacía llamada a, si no que creamos una lista vacía y se la asignamos al nombre de variable a
a = []
# Ergo aquí se dice que a b se le asigna el mismo valor asignado a a, la lista vacia
b = a

# Podemos confirmarlo si imprimimos el id de ambas variables, devuelven el mismo número,
# por lo que tienen asignados el mismo valor, ambos son nombres para el mismo objeto.
print(id(a))
print(id(b))

# Si modificamos uno de los dos nombres, el otro también verá el mismo cambio
a.append(35)

print(a)  # Imprime [35], como era de esperar
print(b)  # También imprime [35]


# Si ahora creamos una lista vacía para b, b pasa a tener asignada una lista nueva, separada de la de a
b = []

print(id(a))  # Aquí imprimen ids distintos
print(id(b))

print(a)  # Imprime [35], como antes
print(b)  # Imprime []

"""
En Python todo se puede redefinir, es mutable, excepto aquello definido específicamente como inmutable; enteros, flotantes, tuplas, cadenas de caracteres, booleanos...
"""

a = 12345  # Crea un espacio de memoria con el valor 12345 y lo asigna al nombre a
b = 12345  # Asigna el mismo espacio a b

print(id(a))  # Ambos imprimen el mismo id
print(id(b))

a = 12346  # Crea otro espacio de memoria con el valor 12346 y lo asigna al nombre a

print(id(a))  # Ahora imprimen ids distintos
print(id(b))


a = "Hola"
b = a

print(id(a))  # Mismo id
print(id(b))

# Aquí no estamos añadiendo nada a la string asignada a a, si no
# creando una completamente nueva que es una combinación de ambas.
a += " mundo"
# Y sabiendo que esto es igual que a = a + " mundo", ahora a tiene un valor completamente nuevo


print(id(a))  # Id distinto
print(id(b))


# En definitiva, cada vez que haces una asignación en Python, realmente lo que estás haciendo es asignar un valor completamente nuevo y una zona de memoria distinta al nombre de la variable
