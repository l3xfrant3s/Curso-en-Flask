"""
En Python no hay que decirle específicamente que estamos
exportando algo, como sí se hace en otros lenguajes.

Comparado con Java, es como si cada archivo fuera su
propio paquete llamado igual que el propio archivo.

Nota mental: no usar guiones en los nombres de los archivos, sobretodo si van a ser importados
"""


def divide(dividend, divisor):
    return dividend / divisor


"""
Usando el método mágico __name__, podemos saber
desde donde se está ejecutando código en Python.
Será útil aquí para averiguar si estamos ejecutando
mi_modulo directamente o desde otro archivo

Si fueras a ejecutar este archivo por sí solo, lo de abajo imprimiría "mi_modulo.py: __main__"
Un valor de __main__ para __name__ significa que estamos ejecutando el mismo archivo
"""
print("mi_modulo.py: ", __name__)
