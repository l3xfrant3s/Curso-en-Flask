from db import db  # Importamos el objeto SQLAlchemy

# Aquí hacemos lo mismo que en item.py, creamos un modelo de tabla SQL


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
