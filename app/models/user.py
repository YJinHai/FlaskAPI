from datetime import datetime

from flask_jwt import JWT
from mongoengine import *
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from werkzeug.security import safe_str_cmp


class User(Document):
    #id = IntField(primary_key=True)
    name = StringField(max_length=200, required=True, unique=True)
    pwd = StringField(max_length=128)
    gold = IntField(max_value=9999, default=0)
    last_seen = DateTimeField(default=datetime.utcnow)

    def hash_password(self, password):
        self.pwd = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.pwd)





