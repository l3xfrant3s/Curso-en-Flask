day_of_week = input("What day of the week is it today? ").lower()

if day_of_week == "monday":
    # Los dos puntos del if definen un bloque de código (como las llaves en muchos otros lenguajes)
    print("Have a great start to your week!")
# Este bloque debe estar siempre una indentación más adentro, o se considerará que está fuera del bloque

elif day_of_week == "wednesday":
    print("It is Wednesday my dudes")

else:
    print("Full speed ahead!")

print(f"Today is {day_of_week}")
