# La forma en la que está escrita esta función no es del todo correcta, ya que divisor = 0, más que saltar un error, simplemente te lleva por otro camino.
def divide(dividend, divisor):
    if divisor == 0:
        print("Divisor cannot be 0.")
        return

    return dividend / divisor


# Ahora, este "programa" va a usar la función creada anteriormente para calcular la media de esta lista de notas
grades = [78, 99, 85, 100]  # Con esta lista para las notas, va a imprimir:
# Welcome to the average grade program.
# The average grade is 90.5

print("Welcome to the average grade program.")
average = divide(sum(grades), len(grades))

print(f"The average grade is {average}")
print("\n")

# Pero si hacemos que la lista esté vacia, va a imprimir:
# Welcome to the average grade program.
# Divisor cannot be 0.
# The average grade is None

# Ahora mi pregunta es, ¿qué más le dará al usuario que el divisor sea 0, cuando está trabajando con una lista de notas?

# Lo suyo sería modificar el programa para que le diga al usuario el problema real, que no ha enviado ninguna nota
# Pero la cosa se está volvería confusa para el programador
grades = []

print("Welcome to the average grade program.")
average = divide(sum(grades), len(grades))

print(f"The average grade is {average}")


# En su lugar lo que vamos a hacer es usar errores


def divide(dividend, divisor):
    if divisor == 0:
        # Usando la función raise, podemos forzar que ocurran errores o excepciones.
        # En este caso, forzamos un error ZeroDivisionError con el mensaje "Divisor cannot be 0."
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


# Si intentamos calcular la media de las notas usando una lista vacía otra vez, va a ocurrir el error que estamos forzando.
# Cuando esto ocurre, se va a mostrar por consola qué líneas causaron el error (el traceback) y el propio error.
grades = []

print("Welcome to the average grade program.")
# average = divide(sum(grades), len(grades)) # <- Esta línea es la problemática

print(f"The average grade is {average}")


# Ahora, podemos "capturar" el error y hacer algo cuando ocurra
# La forma en la que se hace es con un bloque try-except, similar al bloque try-catch en Java
grades = []
print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is {average}")
except ZeroDivisionError as zde:
    # Así podemos mostrar el mensaje del error, el objecto del error puede llamarse como quieras, hay gente que los llama
    # e de error o excepción, a mi me gusta llamarlos una abreviatura del nombre del error, como aquí, zde de ZeroDivisionError.
    print(zde)
    print("There are no grades yet in your list.")


# Hay más tipos de errores, como TypeError, ValueError, RuntimeError o los que son creados por el programador


# Podemos añadir un bloque else, para separar el código que puede tirar errores en el try del que no
# También podemos añadir un bloque finally, que funciona al contrario que el else, siempre se ejecuta hayan ocurrido errores o no, después que el resto

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as zde:  # Podemos añadir tantos bloque except como querramos, para capturar varios errores distintios
    print(zde)
    print("There are no grades yet in your list.")
else:  # Este bloque solo corre si no se ha metido en ningún except
    print(f"The average grade is {average}")
finally:  # Este bloque siempre se ejecuta, después de todo lo demás
    print("Thank you!")
