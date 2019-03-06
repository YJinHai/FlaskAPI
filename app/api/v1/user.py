import datetime

from flask import g, request
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource, reqparse

from app.libs.redprint import Redprint
from app.models.user import User

api = Redprint('user')


class UserAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True,
                                   help='No username provided', location='form')
        self.reqparse.add_argument('pwd', type=str, required=True,
                                   help='No user password provided', location='form')

        super(UserAPI, self).__init__()

    def post(self):
        pass

    def get(self, id):
        user = User.objects(id=id).first()

        return {'name': user.name,
                'id': user.id.__str__()}, 200

    @jwt_required
    def put(self, id):
        pass

    @jwt_required
    def patch(self, id):
        user = User.objects(id=id).first()
        user.gold = int(request.form['gold'])
        user.save()
        return {'msg': user.gold}

    def delete(self, id):
        pass
