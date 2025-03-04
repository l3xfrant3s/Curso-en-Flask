"""
Aquí, sin embargo, es posible porque, cuando ejecutamos importar_relativo, "mi_libreria" y "operaciones" sí están en una carpeta, "librerias".
Si lo fueramos a ejecutar directamente tiraría el mismo error que los anteriores.

De fondo lo que ocurre cuando es que Python toma la ruta del archivo, quita la parte del módulo actual y añade lo que pongas en el import.
"""

from .operaciones import operador  # noqa: F401

print("mi_libreria.py:", __name__)
