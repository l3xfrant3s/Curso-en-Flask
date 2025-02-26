number = 7

while True:
    user_input = input('Introduce "S/n" si quieres jugar: ')

    if user_input == "n":
        break

    user_number = int(input("Estoy pensando en un número... "))
    if user_number == number:
        print("¡Cooorrecto!")
    elif abs(number - user_number) == 1:
        print("Ahhhh que cerca, por uno.")
    else:
        print("Lo siento, se ha equivocado.")
