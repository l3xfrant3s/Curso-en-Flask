# Aunque los 3 se parecen, la diferencia principal entre una lista y una tupla es que la tupla es inmutable una vez
# declarada; la diferencia entre una lista y una coleccion es que no puede haber elementos duplicados en la coleccion
# y que no se pueden modificar pero sí añadir

lista = ["Baldwin", "Adrián", "Alexis"]
tupla = ("Baldwin", "Adrián", "Alexis")
coleccion = {"Baldwin", "Adrián", "Alexis"}

print(lista[0])  # Va a imprimir "Baldwin"
print(tupla[1])  # Va a imprimir "Adrián
# print(coleccion[0]) no va a funcionar

lista[0] = "Francisco Javier"  # Esto no es posible con las tuplas o las colecciones

print(lista[0])  # Va a imprimir "Francisco Javier"

lista.append("Baldwin")

print(lista[3])  # Va a imprimir "Baldwin"

lista.remove("Francisco Javier")

coleccion.add("Francisco Javier")
coleccion.add("Francisco Javier")
print(
    coleccion
)  # Va a imprimir toda la colección en un orden cualquier, además notese que "Francisco Javier" solo aparece una vez
