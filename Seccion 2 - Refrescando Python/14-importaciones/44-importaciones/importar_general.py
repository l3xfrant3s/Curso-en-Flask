"""
Así se importa y usa un archivo entero en Python.
En uso, es similar a un método de clase.
"""

import mi_modulo

print(mi_modulo.divide(10, 2))

"""
Aquí ocurre lo mismo que en el import específico, mi_modulo va a imprimir "mi_modulo.py: mi_modulo" porque no es parte del mismo archivo.

Y el de debajo va a imprimir "importar_general.py:, __main__" porque está en el mismo archivo que estamos ejecutando.
"""

print("importar_general.py:", __name__)
