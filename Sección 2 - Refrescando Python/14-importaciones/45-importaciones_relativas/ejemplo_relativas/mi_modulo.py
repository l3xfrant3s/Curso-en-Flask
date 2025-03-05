"""
Va a ocurrir lo mismo aquí si intentamos hacer una importación relativa de "librerias".

Abajo pone "En la misma carpeta que este archivo, buscar un paquete llamado librerias y trae el módulo mi_libreria".

Pero también tirará un error porque, según Python, no estamos en una carpeta o paquete.
"""

from librerias import mi_libreria  # noqa: F401


def dividir(dividendo, divisor):
    return dividendo / divisor


print("mi_modulo.py: ", __name__)
