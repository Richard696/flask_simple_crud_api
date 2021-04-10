from .db import db 

class User(db.Document):
    userName = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)

class Product(db.Document):
    productName = db.StringField(required=True, unique=True)
    productImgUrl = db.StringField(required=True)