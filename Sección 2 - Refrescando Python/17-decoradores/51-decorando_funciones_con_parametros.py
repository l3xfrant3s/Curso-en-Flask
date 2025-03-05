import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
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


# Si ahora probamos funciones con parámetros, tenemos el problema de que la función
# que la sustituye no toma ninguno, por lo que esta nueva función tampoco lo hará
@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


# A pesar de que la habíamos definido con un parámetro, dará un error porque no espera ninguno
# print(get_password("admin")) # Comentado para que no de error en mi ejecución del código


# Una solución podría ser redefinir el decorador para que acepte y pase un parámetro a la nueva función
def make_secure(func):
    @functools.wraps(func)
    def secure_function(panel):
        if user["access_level"] == "admin":
            return func(panel)
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


# Lo cual funciona con funciones de un parámetro
@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


print(get_password("admin"))  # Ahora no da error


# Esto no es ideal porque ahora make_secure solo sirve para funciones de un parámetro
@make_secure
def get_admin_password():
    return "1234"


# A pesar de no tener ninguno en su definición, tira error porque espera uno
# print(get_admin_password()) # Comentado para que no de error en mi ejecución del código


# La única solución entonces, es hacer que la función nueva acepte argumentos infinitos
def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


@make_secure
def get_admin_password():
    return "1234"


# Ahora puedo declarar y usar funciones con tantos argumentos como quiera
print(get_password("admin"))
print(get_admin_password())
