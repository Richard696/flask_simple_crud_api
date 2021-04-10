from .db import db


class User(db.Document):
    username = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    role = db.IntField(require=True)
