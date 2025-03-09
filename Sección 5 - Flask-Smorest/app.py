from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)

# De aquí se borró todo menos la definición de app
# Aquí, ahora, se van a definir ciertas opciones de cara a la documentación usando Swagger UI

# Propagar excepciones que ocurran en alguna extensión de Flask
app.config["PROPAGATE_EXCEPTIONS"] = True
# Título de la documentación
app.config["API_TITLE"] = "Stores REST API"
# Versión de la documentación
app.config["API_VERSION"] = "v1"
# Versión de OpenAPI
app.config["OPENAPI_VERSION"] = "3.0.3"
# Dónde está la raíz de la documentación para que lo sepa la documentación
app.config["OPENAPI_URL_PREFIX"] = "/"
# Le dice que use Swagger UI para la documentación
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
# Le dice que cargue el código de Swagger UI de esa URL
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# Conecta la aplicación con la API, matando dos pájaros de un tiro al traer las rutas de store.py e item.py y las usa y las documenta
api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)

# Y con todo eso hecho, si corremos la aplicación, ya sea con flask run en la consola o en un contenedor de Docker, ahora podemos acceder a la documentación en http://localhost:5005/swagger-ui (Puerto 5005 porque es el que uso para redirigir el tráfico del contenedor Docker)
