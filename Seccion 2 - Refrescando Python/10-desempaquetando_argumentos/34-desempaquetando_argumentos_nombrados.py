"""
Dos asteriscos en los argumentos de la declaración de una función indican
que se está esperando una cantidad indefinida de argumentos nombrados.
Se convertirán en un diccionario, tomando el nombre del parámetro como
clave y el valor asignado como valor del par, efectivamente empaquetándolo.
"""


def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)  # Va a imprimir "{'name': 'Bob', 'age': 25}"


def named(name, age):
    print(name, age)


"""
Usando los mismos asteriscos en la llamada, se puede pasar un diccionario como argumentos nombrados, desempaquetándolo.
"""

details = {"name": "Bob", "age": 25}

named(**details)  # named(name="Bob", age=25)


# Se pueden usar a la vez en ambos sitios
def named(**kwargs):
    print(kwargs)


named(**details)


# kwargs aquí funciona como cualquier otro diccionario
def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


# Puedes usar a la vez un asterisco para los argumentos posicionales y dos asteriscos para los nombrados
def both(*args, **kwargs):
    print(args)
    print(kwargs)


# Se sigue aplicando la norma de que los argumentos posicionales se ponen antes
# que los nombrados, aunque ahora aceptaría un número potencialmente ilimitado de argumentos

both(1, 3, 5, name="Bob", age=25)

"""
def post(url, data=None, json=None, **kwargs):
    return request("post", url, data=data, json=json, **kwargs)
"""
