x = 5, 11  # Esto va a crear una tupla
# Si no se rodean los números explicitamente con corchetes
# o llaves, Python asume que se trata de una tupla

x, y = 5, 11  # Esto va a crear dos variables
# Equivale a:
# x = 5
# y = 11

t = 5, 11  # Crea una tupla
x, y = t  # x = t[0], y = t[1]


student_attendance = {"Rolf": 96, "Adam": 80, "Anne": 100}

# student_attendance.items() devuelve una lista de tuplas; un bucle for,
# al iterar entre cada elemento de la lista (cada tupla), es posible
# desestructurarla para obtener cada elemento en una variable distinta
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


people = [
    ("Bob", 42, "Mechanic"),
    ("James", 24, "Artist"),
    ("Harry", 32, "Lecturer"),
]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Saltará un error si falta cualquiera de los valores en la tupla, por ejemplo
# people = [
#     ("Bob", 42),
#     ("James", 24, "Artist"),
#     ("Harry", 32, "Lecturer"),
# ]

# Desestructurar la lista people es equivalente a hacer lo siguiente:
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

person = ("Bob", 42, "Mechanic")

# Se usa _ como nombre de variable cuando se
# quiere reflejar que esa variable va a ser ignorada.
# Es un nombre de variable perfectamente válido, nada
# te impide usarla, aunque se considera mala práctica
name, _, profession = person

print(name, _, profession)

# Va a guardar el primer valor en head, y el resto en tail
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

# Si ponemos el asterisco en head en vez de tail, va guardar tantas variables
# como pueda en head, reservando las que hagan falta en las demás variables
*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
