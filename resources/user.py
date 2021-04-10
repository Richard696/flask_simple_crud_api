from flask import Blueprint, jsonify, request, Response
from database.model import User
import bcrypt

users = Blueprint('users', __name__)


@users.route('/v1/user')
def get_User():
    user = User.objects().to_json()
    return Response(user, mimetype="application/json", status=200)


# reference to encrypt the password https://stackoverflow.com/questions/27943258/save-password-as-salted-hash-in-mongodb-in-users-collection-using-python-bcrypt
# more info regarding bcrypt package -> https://pypi.org/project/bcrypt/
@users.route('/v1/user', methods=['POST'])
def add_user():
    body = request.get_json()
    body.password = bcrypt.hashpw(body.password, bcrypt.gensalt())
    user = User(**body).save()
    id = user.id
    return jsonify({
        "status": 200,
        "id": id,
        "message": "Successfully create the user"
    })


@users.route('/v1/user/<id>', methods=['PUT'])
def update_user():
    body = request.get_json()
    User.objects.get(id=id).update(**body)
    return jsonify({
        "status": 200,
        "message": "Successfully update the user"
    })


@users.route('/v1/user/<id>', methods=['DELETE'])
def delete_user():
    body = request.get_json()
    User.objects.get(id=id).delete()
    return jsonify({
        "status": 200,
        "message": "Successfully delete the user"
    })
