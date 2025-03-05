"""
En Python, puedes hacer con las funciones las mismas cosas que podrías hacer con cualquier otro tipo de variable,
como asignarlas a otras variables, por lo tanto, es posible pasar funciones como parámetros a otra función.
"""

# Aquí debajo tenemos un ejemplo de eso mismo, la función divide se pasa como parámetro a calculate, para ser llamada dentro de la función


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)  # Sólo aquí ocurre la llamada a la función


result = calculate(20, 4, operator=divide)  # Notese que no lleva paréntesis divide
"""
Estas funciones pasadas como parámetros tienen las mismas limitaciones que la función de base.
En este caso, no se pueden pasar más de dos parámetros para values porque divide solo acepta dos parámetros
si lo hacemos saltará el error de los argumentos inesperados.
"""
print(result)


# Otro ejemplo, con una función que busca dentro de una secuencia un elemento usando otra función que pasamos como parámetro

from operator import itemgetter


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]


def get_friend_name(friend):
    return friend["name"]


# Además de funciones que creamos nosotros mismos, podemos usar funciones lambda
# y declararlas en la llamada a search, o funciones importadas de otro lado.

# Todas estas son formas válidas de usar esta función
print(search(friends, "Rolf Smith", get_friend_name))
print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
print(search(friends, "Rolf Smith", itemgetter("name")))
