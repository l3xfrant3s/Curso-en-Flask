number = 7

# user_input = input('Introduce "s" si quieres jugar: ')
user_input = input('Introduce "s" si quieres jugar: ').lower()

if user_input == "s":
    # user_input in ("s", "S")
    user_number = int(input("Estoy pensando en un número... "))
    if user_number == number:
        print("¡Cooorrecto!")
    elif abs(number - user_number) == 1:
        # number - user_number in (1, -1)
        print("Ahhhh que cerca, por uno.")
    else:
        print("Lo siento, se ha equivocado.")
