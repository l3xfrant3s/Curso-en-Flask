import uuid

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import stores
from schemas import StoreSchema

# Un Blueprint se usas para dividir una API en varios segmentos. Este es otro método que también existe en Flask, a falta de algún añadido en F-Smorest.
# MethodView se usa para crear clases cuyos métodos se dirijan a ciertos endpoints

# Combinando ambas, se puede ver que hemos divido la API en 4 clases, cada una dedicada a una url y dentro de las cuales se ponen todos los métodos que se dirigen a esa url.

blp = Blueprint("Stores", __name__, description="Operations on stores")
# Se crea un blueprint, dándole un nombre para la documentación, un nombre bajo el que se exportará y una descripción para la documentación.


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    # Cada método dentro de la clase se llama igual que el método HTTP correspondiente
    # Dentro de cada uno va el mismo código que tenían en app-previo-blp.py
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found.")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    # Escrito después de usar marshmallow, algunos métodos han sido cambiados para usar los Schemas
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema())
    def post(self, store_data):
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message="This store already exists")

        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store
