from flask import Flask
from flask_jwt import JWT
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_restful import Api

from app.api.v1 import API_VERSION_V1
from app.models.user import User
from config import Config
# from api.database import db


api = Api()


# mongo = PyMongo()

def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(
        create_blueprint_v1(),
        url_prefix='{prefix}/v{version}'.format(
            prefix=app.config['URL_PREFIX'],
            version=API_VERSION_V1))


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api.init_app(app)
    jwt = JWTManager(app)

    # mongo.init_app(app)
    register_blueprints(app)



    app.run(host='0.0.0.0', port=8000, debug=True)
