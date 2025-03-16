from db import db  # Importamos el objeto SQLAlchemy

# Creamos un modelo de tabla SQL con las propiedades que ya hemos visto en lecciones anteriores


class ItemModel(db.Model):  # Todos los modelo heredan de db.Model
    __tablename__ = "items"  # La tabla se llamará items

    # El id es una columna de tipo entero y clave primaria
    id = db.Column(db.Integer, primary_key=True)
    # El nombre es una columna de tipo cadena de longitud 80, valores únicos y no nulos
    name = db.Column(db.String(80), unique=True, nullable=False)
    # El precio es una columna de tipo flotante con dos cifras después de la coma, valores no únicos y no nulos
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    # El id de la tienda es una columna de tipo entero valores no únicos y no nulos
    store_id = db.Column(db.Integer, unique=False, nullable=False)
