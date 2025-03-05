edad = int(input("¿Cuántos años tienes?: "))
meses = edad * 12
segundos = edad * 31557600  # 365.25 * 24 * 60 * 60
print(f"Tienes {edad} años, lo que equivale a {meses} meses o {segundos:,} segundos")
