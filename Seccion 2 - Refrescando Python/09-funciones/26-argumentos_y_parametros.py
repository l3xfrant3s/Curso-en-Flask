def add(x, y):  # Se ponen los parámetros entre los paréntesis
    # pass # Se usa pass para decirle a la función que no haga nada
    result = x + y
    print(result)


add(5, 3)  # Cuando se llame, hay que poner algo entre los de aquí también


def say_hello():
    print("Hello!")


say_hello()  # Si no se pone nada en los parámetros al definir la
# función, entonces no se deben pasar ninguno al llamarla tampoco


def say_hello(name, surname):
    print(f"Hello {name} {surname}!")


say_hello(surname="Felipe", name="Alexis")

# En Python se pueden pasar argumentos posicionales, es decir, su posición en la llamada determina qué parámetro es, o argumentos nombrados,
# que se usan para pasar argumentos en un orden distinto al de declaración y para aclarar un poco qué hace una función llamada


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


# Se recomienda usar argumentos nombrados para facilitar la lectura del código
divide(dividend=15, divisor=0)
