import uuid

from flask import Flask, request

from db import items, stores

app = Flask(__name__)


@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex  # Genera un nuevo id
    # Crea la tienda con los datos recibidos por JSON y el id
    store = {**store_data, "id": store_id}
    stores[store_id] = store  # Guarda la tienda usando el id como clave
    return store, 201


@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201


@app.get("/store")
def get_all_stores():
    return {"stores": list(stores.values())}


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


@app.get("/stores/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:  # Saltará KeyError si no encuentra una clave en el diccionario
        return {"message": "Store not found"}, 404


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message": "Item not found"}, 404
