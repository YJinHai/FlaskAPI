from flask import Flask, Blueprint
from flask_restful import Api

from app.api.v1 import user
from app.api.v1.login import LoginAPI
from app.api.v1.register import RegisterAPI
from app.api.v1.user import UserAPI

API_VERSION_V1 = 1
API_VERSION = API_VERSION_V1


def create_blueprint_v1():
    api_v1_bp = Blueprint('api_v1', __name__)

    user.api.register(api_v1_bp)

    api = Api(api_v1_bp)

    api.add_resource(RegisterAPI, '/register', endpoint='register')

    api.add_resource(LoginAPI, '/login', endpoint='login')

    api.add_resource(UserAPI, '/user', '/user/<string:id>', endpoint='user')

    return api_v1_bp
