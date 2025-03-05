"""
Así se importan y usan partes específicas de un archivo en Python.
Es como si la función importada fuera parte del mismo archivo que la importa.
"""

import sys

import mi_modulo_y_libreria  # noqa: F401 # Esta nota es para que Ruff no elimine automáticamente el import no usado
from mi_modulo import divide

print(divide(10, 2))

"""
Si ejecutamos este archivo, mi_modulo, que tiene un print de __name__, va a imprimir "mi_modulo.py: mi_modulo",
acorde al nombre de su archivo porque realmente no es parte del archivo que estamos ejecutando, si no que es importado de mi_modulo.

Sin embargo este de aquí debajo, al estar en el archivo que estamos ejecutando, va a imprimir "importar_especifico.py:, __main__".
"""

print("importar_especifico.py:", __name__)


# El orden de impresión aquí es: cualquier módulo que ya exista en Python por defecto, como sys -> los módulos que hayas creado tú
print(sys.modules)
