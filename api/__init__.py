
from api.views import blueprint
from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager

app = Flask(__name__)
Swagger(app)
jwt = JWTManager(app)
app.register_blueprint(blueprint, url_prefix='/api/v1')
app.config['JWT_SECRET_KEY'] = 'this-is-confidential'
