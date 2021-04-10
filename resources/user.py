from flask import jsonify, request, Response
from flask_restful import Resource
from database.model import User
from flask_bcrypt import generate_password_hash


class UsersApi(Resource):

    def get(self):
        user = User.objects().to_json()
        return Response(user, mimetype="application/json", status=200)

    # reference to encrypt the password https://stackoverflow.com/questions/27943258/save-password-as-salted-hash-in-mongodb-in-users-collection-using-python-bcrypt
    # more info regarding bcrypt package -> https://pypi.org/project/bcrypt/

    def post(self):
        body = request.get_json()
        print("Content of the request:")
        print(body)
        password_hash = generate_password_hash(body.get('password'))
        body['password'] = password_hash
        user = User(**body).save()
        id = user.id
        return {'msg': 'user is created successfully', 'id': str(id)}, 200


class UserAPI(Resource):
    def put(self, id):
        body = request.get_json()
        User.objects.get(id=id).update(**body)
        return jsonify({
            "status": 200,
            "message": "Successfully update the user"
        })

    def delete(self, id):
        body = request.get_json()
        User.objects.get(id=id).delete()
        return jsonify({
            "status": 200,
            "message": "Successfully delete the user"
        })
