friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)

# .difference va a descartar aquellos elementos que están en ambas colecciones

print(local_friends)
