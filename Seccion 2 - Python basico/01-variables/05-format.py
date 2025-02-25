name = "Bob"
greeting = "Hello, {}"  # Guarda una plantilla
with_name = greeting.format(
    name
)  # Llamando a format, va a reemplazar las llaves por lo que pasemos como parámetro

print(with_name)

saludo = "Eres {}, ¿no?"
con_nombre = saludo.format("Alexis")

print(con_nombre)

frases_largas = "Hola {}, hoy estamos viendo {}"  # se pueden usar para crear strings más largas, con más parámetros
preparada = frases_largas.format("Adrián", "strings formateadas")

print(preparada)
