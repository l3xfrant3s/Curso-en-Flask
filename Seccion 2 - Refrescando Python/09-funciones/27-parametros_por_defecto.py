# Al darle un valor a un parámetro, este se convierte en opcional
# Si no se le da ningún valor, se considera obligatorio
# Además, se deben declarar los obligatorios primero
# def add(x=8, y): dará un error
def add(x, y=8):
    print(x + y)


# En la llamada a la función debe haber un argumento posicional,
# o nombrado, pero podemos saltarnos "y" y usará el valor dado en la definición
# add(x=4, 8) dará un error
add(x=5)
