from marshmallow import Schema, fields

# Los Schemas de marshmallow se usan para facilitar la validación de los datos recibidos o enviados.

# Aquí se define una clase heredera de Schema por cada tipo de operación distintiva que use un grupo distinto de datos, similar a como se separaban las clases al usar Blueprints.


class ItemSchema(Schema):
    # Se marca dump_only si es un campo solo de lectura, nunca será enviado por el usuario.
    id = fields.Str(dump_only=True)
    # Se marca required si el usuario debe enviarlo.
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    # No se pone nada si es opcional.
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
