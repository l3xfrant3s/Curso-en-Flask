edad = int(input("¿Cuántos años tienes?: "))
meses = edad * 12
segundos = int(meses * 31557600)
print(f"Tienes {edad} años, lo que equivale a {meses} meses o {segundos:,} segundos")
