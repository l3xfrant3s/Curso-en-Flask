from flask import Flask, request

# Creamos una aplicación de Flask, así le decimos a Flask que use este archivo para los endpoints
app = Flask(__name__)


stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


# Definimos un endpoint para obtener la lista de tiendas,
# la función de app será el método HTTP que vaya a usar y
# dentro se pone la dirección en la que podremos acceder a ello
# En este caso, por el método GET y en la dirección (como estoy trabajando en local) localhost:5000/stores
# Si accedemos a esa dirección, nos devolverá un JSON con los mismos datos asignados a stores
@app.get("/stores")
def get_stores():
    return {"stores": stores}


# Aquí definimos un endpoint para cuando se vayan a recibir datos en su lugar.
# Como los datos se envían y se reciben por JSON, hay que recoger los datos del JSON.
# Los datos recibidos se convierten en un diccionario de Python automáticamente.
# Por último, después de insertarlos en nuestra lista que está actuando como base de datos, hay que devolver algo.
# Este método debe devolver algo y un código HTTP, así que vamos a devolver
# la tienda creada y el código HTTP 201, que significa "Recurso creado con éxito".
@app.post("/stores")
def create_store():
    request_data = request.get_json()  # request se importa de Flask, con el método get_json se convierte a diccionario de Python
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


# En Insomnia, estoy probando con este JSON:
# {
#   "name": "My Store"
# }
# a esta url: http://localhost:5000/stores


# Con este endpoint, estamos creando un nuevo elemento en una tienda existente
# Poniendo en la URL <string:name> y luego definiendo el parámetro name,
# hace estén conectados y podamos usas ese valor dentro de la función.
@app.post("/stores/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:  # Recorrerá la lista de tiendas
        if store["name"] == name:  # En busca de una que se llame igual que name
            # Si la encuentra, creará un nuevo artículo
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            # Y lo añadirá a la lista de items de la tienda correspondiente
            store["items"].append(new_item)
            return new_item, 201
    # Si no la encuentra en toda la lista, enviará un mensaje de error
    return {"message": "Store not found"}, 404


# En Insomnia, estoy probando con este JSON:
# {
#   "name": "Table",
#   "price": 17.99
# }
# a esta url: http://localhost:5000/stores/My Store/item

# Y este JSON:
# {
#   "name": "Laptop",
#   "price": 1799
# }
# a esta url: http://localhost:5000/stores/My Store 2/item, después de haber creado la tienda correspondiente


# Usando lo aprendido anteriormente, vamos a crear un par de endpoints para obtener los datos de una tienda y los artículos una tienda
@app.get("/stores/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/stores/<string:name>/item")
def get_store_items(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
            # Es preferíble devolver un diccionario con un solo elemento por si queremos modificar este return en el futuro.
    return {"message": "Store not found"}, 404
