friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)
# in buscará el elemento que pongamos antes en la estructura de datos que pongamos después
print("Jen" in "Jennifer")

movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")
print(user_movie in movies_watched)

# funciona tanto en contenedores (listas, tuplas y colecciones) como en strings
