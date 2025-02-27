# Un asterisco en los argumentos de la declaración de una función
# indica que ese argumento es una tupla conteniendo todo lo que
# pasemos como parámetro, sin esperar una cantidad específica.
# A este proceso se le llama empaquetado, ya que combina multiples argumentos en una sola tupla.


def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(1, 3, 4))  # Imprime 12
print(multiply(2, 5, 3, 12, 10))  # Imprime 3600

# El mismo asterisco se puede usar al llamar una función
# en una lista para convertirla en varios argumentos,
# en un proceso llamado desempaquetado.


def add(x, y, z):
    return x + y + z


nums = [3, 5, 7]
print(add(*nums))  # Imprime 15, y es equivalente a vvvvvv
print(add(nums[0], nums[1], nums[2]))

# También funciona con argumentos nombrados, si usamos un diccionario
# cuyas claves se llamen igual que los parámetros de la función

nums = {"x": 3, "y": 5, "z": 7}

print(add(**nums))  # Imprime 15, y equivalente a vvvvvv
print(add(x=nums["x"], y=nums["y"], z=nums["z"]))


# Podemos poner más parámetros, y estos deben ser nombrados cuando se pasen como parámetro
def apply(*args, operator):
    if operator == "*":
        # Recuerda que el parámetro args es una tupla, y que multiply espera multiples variables, por lo que hay que desemepaquetar args aquí
        return multiply(*args)
    elif operator == "+":
        return add(args)
    else:
        return "No valid operator provided to apply()."


# Si no pasamos operator como parámetro nombrado,
# será pasado como parte de args, y eso podría
# llevar a más problemas si no se controla
print(apply(1, 3, 6, 7, operator="*"))
