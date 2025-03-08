# En este archivo especificamos cómo se va a crear la imagen Docker. Abajo pone, en orden:
# USANDO la imagen existente llamada "python", versión 3:13
# EXPONER el puerto interno 5000
# TRABAJAR EN el directorio interno "/app", aquí ocurrirán las siguientes acciones
# EJECUTAR el comando "pip install flask"
# COPIAR el contenido de la carpeta actual ("Sección 4 - Docker") a la carpeta actual dentro del contenedor (como se especificó antes, "/app")
# EJECUTAR "flask run --host 0.0.0.0" cada vez que corra el contenedor, la dirección de host 0.0.0.0 es para que pueda conectarse cualquiera a la aplicación Flask.
FROM python:3.13 
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]