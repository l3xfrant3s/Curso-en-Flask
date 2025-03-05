"""
Aquí podemos hacer lo siguiente:

Los dos puntos dicen que vayamos una carpeta hacia atrás con respecto a la del archivo importador
(en este caso, que busque en librerias, a diferencia de si usaramos el punto, es decir, librerias.operadores)
El asterisco simplemente dice que traiga todo del módulo importado.

Esto solo funciona si ejecutamos importar_relativo o mi_modulo, por razones citadas anteriormente.
"""

from ..mi_libreria import *

print("operator.py: ", __name__)
