from flask import Flask, request

# Creamos una aplicación de Flask, así le decimos a Flask que use este archivo para los endpoints
app = Flask(__name__)


stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


# Definimos un endpoint, la función de app será el método HTTP que vaya
# a usar  y dentro se pone la dirección en la que podremos acceder a ello
# En este caso, por el método GET y en la dirección (como estoy trabajando en local) localhost:5000/stores
# Si accedemos a esa dirección, nos devolverá un JSON con los mismos datos asignados a stores
@app.get("/stores")
def get_stores():
    return {"stores": stores}


# Aquí definimos un endpoint para cuando se vayan a recibir datos en su lugar.
# Como los datos se envían y se reciben por JSON, hay que recoger los datos del JSON.
# Los datos recibidos se convierten en un diccionario de Python automáticamente.
# Por último, después de insertarlos en nuestro diccionario que está actuando como base de datos, hay que devolver algo.
# Este método debe devolver algo y un código HTTP, así que vamos a devolver
# la tienda creada y el código HTTP 201, que significa "Recurso creado con éxito".
@app.post("/stores")
def create_store():
    request_data = request.get_json()  # request se importa de Flask, con el método get_json se convierte a diccionario de Python
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201
