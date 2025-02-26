def hello():
    print("Hello!")


hello()


# Las funciones se crean usando la palabra clave def
def user_age_in_seconds():
    edad = int(input("¿Cuántos años tienes?: "))
    segundos = edad * 31557600  # 365.25 * 24 * 60 * 60
    print(f"Tienes {edad} años, lo que equivale a {segundos:,} segundos")


user_age_in_seconds()

# Se recomienda no usar nombres de funciones ya usadas para nuestras propias funciones
# Por ejemplo:
# def print():
#     print("Hello, world!") <- Ese print ya no es la función de Python, si no la función que acabamos de definir

friends = ["Rolf", "Bob"]


def add_friend():
    friend_name = input("Enter your friend's name: ")
    # friends = friends + [friend_name] <- esto no va a funcionar porque estamos redefiniento friends
    friends.append(friend_name)


add_friend()


# No puedes usar funciones antes de que sean creadas

# hola()  # te va a decir "nuh uh" y tirar un error


def hola():
    print("Hola! :D")


hola()  # ahora sí


def aniadir_numeros():
    numeros.append(10)


# Aunque numeros no esté definido aún, esto es válido porque
# la función se llama después de crear la lista, aunque no parece
# funcionar con enteros

numeros = [1, 2, 3]

aniadir_numeros()
