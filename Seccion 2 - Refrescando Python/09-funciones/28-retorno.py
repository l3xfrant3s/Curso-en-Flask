def add(x, y):
    print(x + y)


# Van a imprimir:
add(5, 8)  # 13
result = add(5, 8)  # 13
print(result)  # None, equivalente a null en muchos otros lenguajes

# Eso pasa porque add no está devolviendo nada, simplemente imprime el resultado


def add(x, y):
    return x + y


# Para ello hay que usar la palabra clave return (como en un millón de otros lenguajes)

add(5, 8)  # No imprime nada
result = add(5, 8)  # Tampoco imprime nada
print(result)  # 13


# return termina completamente la función, por lo que si hay código posteriormente, no se ejecutará
def add(x, y):
    return x + y
    print(x + y)


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


# Es posible tener multiples returns en una función, siempre y cuando estén programados para correr de uno en uno
# Además, y aunque Python no te lo va a impedir, no se recomienda que las funciones devuelvan tipos de datos distintos


result = divide(15, 0)
print(result)
