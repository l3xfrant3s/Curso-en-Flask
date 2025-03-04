"""
Aquí, importar_absoluto importa mi_modulo, mi_modulo importa librerias.mi_libreria, y mi_libreria importa librerias.operaciones.operador.
Cada vez que ocurre un import, deja de ejecutarse el código principal para ejecutar el del archivo importado antes de volver al principal.
De importar_absoluto pasamos a mi_modulo, luego a mi_libreria, y por ultimo a operador, y cuando termina operador, volvemos a importar_absoluto
en orden inverso (operador>mi_libreria>mi_modulo>importar_absoluto), y esto queda reflejado en lo impreso, se ejecuta primero el print de operador,
luego el de mi_libreria, seguido del de mi_modulo y por último el de importar_absoluto.

La forma en la que se importa cada uno de estos archivos se llama importación absoluta, ya que siempre se define la ruta exacta de la que hay que sacar el módulo.
"""

import mi_modulo  # noqa: F401

"""
Va a imprimir:
operador.py:  librerias.operaciones.operador
mi_libreria.py: librerias.mi_libreria
mi_modulo.py:  mi_modulo
importar_absoluto.py: __main__
"""
print("importar_absoluto.py:", __name__)
