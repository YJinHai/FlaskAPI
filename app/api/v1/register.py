from flask_restful import Resource, reqparse

from app.models.user import User
from app.libs.redprint import Redprint

api = Redprint('register')

class RegisterAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True,
                                   help='No username provided', location='form')
        self.reqparse.add_argument('pwd', type=str, required=True,
                                   help='No user password provided', location='form')

        super(RegisterAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        user = User(
            name=args['name'],
        )
        user.hash_password(args['pwd'])
        user.save()

        return {'msg': 'ok'}, 200