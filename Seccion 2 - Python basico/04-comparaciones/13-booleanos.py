print(5 == 5)

print(5 > 5)

print(10 != 10)

# Comparaciones en Python: ==, !=, >, <, >=, <=
# Parecen ser las mismas que en otros muchos lenguajes

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(
    friends == abroad
)  # Comprueba si ambos tienen el/los mismo/s valor/es, es decir, si ambos
# son listas que tienen exactamente los elementos "Rolf" y "Bob", en este caso
print(friends is abroad)  # Comprueba si ambos son la misma lista

abroad = friends
print(friends is abroad)  # Ahora sí devolverá verdadero

friends.append(
    "Alexis"
)  # Al ser ambos instancias del mismo objeto, modificar uno también modifica el otro
print(abroad)
print(friends)
print(abroad is friends)
