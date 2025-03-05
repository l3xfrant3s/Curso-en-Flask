friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]

print(friends[1]["name"])  # Imprime "Adam"

student_attendance = {"Rolf": 96, "Adam": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

# Alternativamente:

# .items() convierte el diccionario en una lista de tuplas clave/valor
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class.")

# Usando la función .values(), obtenemos una lista con los valores sin sus claves
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))
