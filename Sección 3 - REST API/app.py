from flask import Flask

# Creamos una aplicación de Flask, así le decimos a Flask que use este archivo para los endpoints
app = Flask(__name__)


stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


# Definimos un endpoint, la función de app será el método HTTP que vaya
# a usar  y dentro se pone la dirección en la que podremos acceder a ello
# En este caso, por el método GET y en la dirección (como estoy trabajando en local) localhost:5000/stores
@app.get("/store")
def get_stores():
    return {"stores": stores}


# Si accedemos a esa dirección, nos devolverá un JSON con los mismos datos asignados a stores
