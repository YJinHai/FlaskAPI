import datetime

from flask import request, g
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from app.models.user import User
from app.libs.redprint import Redprint

api = Redprint('login')


class LoginAPI(Resource):

    def post(self):
        if not request.is_json:
            return {"msg": "Missing JSON in request"}, 400

        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not username:
            return {"msg": "Missing username parameter"}, 400
        if not password:
            return {"msg": "Missing password parameter"}, 400

        user = User.objects(name=username).first()

        if user is None:
            return {"msg": "Bad username"}, 401
        if not user.verify_password(password):
            return {"msg": "Bad password"}, 401

        expires = datetime.timedelta(seconds=600)
        access_token = create_access_token(user.name, expires_delta=expires)
        return {'access_token': access_token}, 200
