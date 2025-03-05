numbers = [1, 3, 5]
doubled = []

# for num in numbers:
#     doubled.append(num * 2)
# Este sería el método "tradicional" pero se puede recortar usando comprensión de listas

doubled = [n * 2 for n in numbers]

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [f for f in friends if f.startswith("S")]
# Equivale a:
# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

# La comprensión de listas crea una lista nueva, incluso si
# se acaba usando todos los elementos de la lista original
# Dos listas no son la misma aunque contengan exactamente los mismos elementos

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [f for f in friends if f.startswith("S")]

print(friends)
print(starts_s)
print(friends in starts_s)
print("friends: ", id(friends), "starts_s: ", id(starts_s))
