name = input(
    "Enter your name: "
)  # Imprime lo que se pone entre los paréntesis y espera a que
# el usuario escriba algo, luego lo asigna a la variable

print(name)


size_input = input("How big is your house (in square feet): ")
# square_metres = size_input / 10.76   si intentamos hacer esto, altará un error de conversion de string a float
square_feet = float(size_input)
square_metres = square_feet / 10.76
print(square_metres)

# desafio: imprimir algo menos simplón
print(
    f"You house is {square_feet} square feet, which is roughly {square_metres:.2f} square metres."
)  # :.2f indica que queremos formatear el número, en este caso, para que tenga 2 cifras después de la coma
