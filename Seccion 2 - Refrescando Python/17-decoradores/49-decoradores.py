"""
Los decoradores se usan para extender el comportamiento de funciones o métodos sin cambiar el código original.
Se escriben como funciones definidas dentro de otras funciones.
"""

# La idea general de este código es impedir la obtención de la contraseña de administrador a no administradores
user = {"username": "jose", "access_level": "guest"}


def get_admin_password():
    return "1234"


# Un primer instinto podría ser comprobar el nivel de acceso manualmente
if user["access_level"] == "admin":
    print(get_admin_password())
# Es la forma menos complicada de hacer, pero tendrás que poner ese if en cada llamada a get_admin_password


# Otra podría ser definir una función que solo devuelva la contraseña con el nivel de acceso adecuado
def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"


"""
Tienes dos problemillas:
- La función get_admin_password sigue definida ahí arriba, completamente desprotegida, por lo que lo mejor sería borrarla, ¿no? Lo cual lleva al siguiente punto.
- Sigues teniendo el mismo problema de tener que protejer manualmente la obtención de la contraseña; sigues teniendo que escribir el mismo if.
"""


# Usando las funciones de primera clase, podemos reutilizar la función de arriba
def secure_function(func):
    if user["access_level"] == "admin":
        return func


get_admin_password = secure_function(get_admin_password)

# Ahora no podemos usar la función para obtener la contraseña a menos que seamos
# admin, es más, tira un error si eres cualquier otra cosa que no sea admin
print(get_admin_password())
# No es ideal


# Aquí entran en juego los decoradores, que nos permitirán reusar la función de arriba sin modificarla
# o crear un versión segura y sin tener que hacer la misma comprobación de privilegios manualmente.
def make_secure(func):
    def secure_function():  # Ponemos la función que definimos arriba a dentro de otra función
        if user["access_level"] == "admin":
            return func()  # Hacemos que devuelva una llamada en vez de la definición
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function  # Devolvemos la definición de la función interna


get_admin_password = make_secure(get_admin_password)

print(get_admin_password())
