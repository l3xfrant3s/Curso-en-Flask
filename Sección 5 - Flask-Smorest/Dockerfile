# Hemos hecho algunos cambios a este archivo:
# Ahora traemos el archivo requirements.txt primero para instalar todas las extensiones

FROM python:3.13 
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]