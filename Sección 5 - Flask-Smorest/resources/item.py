import uuid

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", __name__, description="Operations on items")

# Vamos a usar los Schemas para validar la entrada de datos de aquellos métodos que reciben datos del usuario
# Estos Schemas también aparecerán en la documentación de Swagger UI


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")

    @blp.arguments(ItemUpdateSchema)
    def put(self, item_data, item_id):
        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort(404, message="Item not found.")


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}

    # Del método post eliminamos el if que comprueba los datos recibidos
    @blp.arguments(ItemSchema)  # En su lugar usamos este decorador
    def post(self, item_data):
        # Y en la definición ponemos un parámetro extra para los datos a validar.
        # Este siempre va después del self y puede llamarse lo que sea.
        # Sustituye el get_json que había antes.
        for item in items.values():
            if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message="This item already exists")

        if item_data["store_id"] not in stores:
            abort(404, message="Store not found.")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item, 201
