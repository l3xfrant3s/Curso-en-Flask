"""
El módulo sys provee a Python de funcionalidad con el sistema.
Provee alternativas a input y print con stdin y stdout,
una forma de recibir argumentos por consola con argv y,
las que vamos a usar ahora, una forma de ver a qué carpetas
puede acceder Python con path y una forma de ver
qué módulos están siendo importado con modules.
"""

import sys

"""
Usando path podemos ver en qué orden Python va a intentar buscar módulos cuando intentas importar algo.
Generalmente será algo así como:
La carpeta en la que se encuentra el archivo importador -> cualquier carpeta que hayas exportado manualmente, definada en PYTHONPATH -> otras carpetas de módulos por defecto
En sistemas UNIX, podemos añadir carpetas a PYTHONPATH usando el comando "export PYTHONPATH=[la carpeta o dirección]"
"""
print(sys.path)
print(sys.modules)
