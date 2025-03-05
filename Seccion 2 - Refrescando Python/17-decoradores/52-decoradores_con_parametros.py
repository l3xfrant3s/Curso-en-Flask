import functools

user = {"username": "jose", "access_level": "guest"}


# Para pasar parámetros a los decoradores, tenemos que envolver el decorador en otra función, que es la que toma los argumentos
# A esta tercera capa de función se le suele llamar fábrica de decoradores
def make_secure(access_level):  # Esta NO es el decorador, solo toma sus argumentos
    def decorator(func):  # El propio decorador, toma la función que será decorada
        @functools.wraps(func)
        def secure_function(*args, **kwargs):  # La función por la que será sustituida
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"

        return secure_function

    return decorator


@make_secure("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


user = {"username": "unregistered user", "access_level": "guest"}

print(get_admin_password())  # No admin permissions for unregistered user
print(get_dashboard_password())  # No user permissions for unregistered user


user = {"username": "jose", "access_level": "user"}

print(get_admin_password())  # No admin permissions for jose
print(get_dashboard_password())  # user: user_password


user = {"username": "ana", "access_level": "admin"}

print(get_admin_password())  # admin: 1234
print(get_dashboard_password())  # No user permissions for ana
