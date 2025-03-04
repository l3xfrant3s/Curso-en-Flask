"""
La gracia de las importaciones relativas es importar de la misma carpeta que el archivo importador, y pongo especial énfasis en "carpeta".
El archivo "importar_absoluto.py" imprimía:

operador.py:  librerias.operaciones.operador
mi_libreria.py: librerias.mi_libreria
mi_modulo.py:  mi_modulo
importar_absoluto.py: __main__

Notese que no hay carpetas en la ruta de importar_absoluto o mi_modulo, pero sí en mi_libreria (librerias) y en operador (librerias.operador).



Las importaciones relativas siempre se hacen en la forma "from [modulo] import [algo]"
El punto significa la misma carpeta que el archivo importador, es decir, abajo pone:
"En la misma carpeta que este archivo, busca uno llamado mi_modulo y trae el módulo dividir"

from .mi_modulo import dividir  # noqa: F401

Si intentamos hacer esta importación ejecutando importar_relativo tirará un error porque, a ojos de Python, no estamos en una carpeta, si no en __main__.
"""

import mi_modulo  # noqa: F401

print("importar_relativo.py:", __name__)


"""
A la única conclusión a la que hemos llegado Jose Salvatierra y yo es que no merecen la pena y
son muy poco flexibles, ya que no los puedes usar en archivos que ejecutas directamente.
Es preferible usar importaciones absolutas.
"""
