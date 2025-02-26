friends = ["Rolf", "Jen", "Bob", "Anne"]

# for friend in range(4):
for friend in friends:
    print(f"¡Hombre {friend}! ¡amigo mío!")


grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

# Todo esto es innecesario en este caso específico,
# existe la funcion sum() para calcular la suma
# de los elementos de una lista o tupla
# total = sum(grades)

print(f"Nota media: {total / amount}")
