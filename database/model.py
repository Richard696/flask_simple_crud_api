from .db import db


class User(db.Document):
    userName = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    role = db.IntField(require=True)
