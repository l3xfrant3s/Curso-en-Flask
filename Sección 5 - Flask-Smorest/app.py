import uuid

from flask import Flask, request
from flask_smorest import abort

from db import items, stores

app = Flask(__name__)


@app.post("/store")
def create_store():
    store_data = request.get_json()

    # Comprobamos que la nueva tienda tiene campo name
    if "name" not in store_data:
        abort(
            400,
            message="Bad request. Ensure 'name' is included in the JSON payload.",
        )

    # Comprobamos que no exista una tienda con el mismo nombre
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message="This store already exists")

    store_id = uuid.uuid4().hex  # Genera un nuevo id
    # Crea la tienda con los datos recibidos por JSON y el id
    store = {**store_data, "id": store_id}
    stores[store_id] = store  # Guarda la tienda usando el id como clave
    return store, 201


@app.post("/item")
def create_item():
    item_data = request.get_json()

    # Comprobamos si el nuevo artículo tiene los campos price, store_id y name
    if (
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(
            400,
            message="Bad request. Ensure 'price', 'store_id' and 'name' are included in the JSON payload.",
        )

    # Comprobamos si ya existe un artículo con el mismo nombre en la tienda que se vaya a crear
    for item in items.values():
        if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(400, message="This item already exists")

    if item_data["store_id"] not in stores:
        # Cambiamos los return de errores 404 por la función de Flask/Flask-Smorest abort
        abort(404, message="Store not found.")

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


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:  # Saltará KeyError si no encuentra una clave en el diccionario
        abort(404, message="Store not found.")


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found.")
