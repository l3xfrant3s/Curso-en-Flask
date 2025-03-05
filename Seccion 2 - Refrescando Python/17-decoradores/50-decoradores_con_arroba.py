user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


def get_admin_password():
    return "1234"


get_admin_password = make_secure(get_admin_password)
# Podemos hacer esto más corto usando una arroba


@make_secure  # Aquí se pone @[función decoradora] para hacer automáticamente lo de arriba
def get_admin_password():
    return "1234"


# Con access_level = guest o cualquier valor que no sea admin, devuelve No admin permissions for jose
print(get_admin_password())
user = {"username": "jose", "access_level": "admin"}
print(get_admin_password())  # Devuelve 1234

# Usar decoradores presenta un problema, y es que la función que pasas a decorador pasa a llamarse internamente igual que la sustituta.
# Es un problema porque hay librerías que usan ese nombre interno.

# Pensarías que esto imprime get_admin_password pero no, imprime secure_function
print(get_admin_password.__name__)

# En este proceso, también se pierde cualquier documentación que hubiera definida para get_admin_password


# Curiosamente la solución es usar otro decorador
import functools  # Este módulo tiene herramientas para trabajar con "objectos llamables"


def make_secure(func):
    # Usando este decorador en la función sustituta, se mantienen el __name__ y la documentación interna
    # Es recomendable usarlo siempre que se vaya a trabajar con decoradores
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password.__name__)  # Ahora imprime get_admin_password

user = {"username": "jose", "access_level": "guest"}
print(get_admin_password())  # Sigue devolviendo No admin permissions for jose
user = {"username": "jose", "access_level": "admin"}
print(get_admin_password())  # Sigue devolviendo 1234
