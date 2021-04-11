from flask import jsonify, request, Response
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from flask_bcrypt import generate_password_hash
from database.model import User
from resources.error import SchemaValidationError, UserNotExistsError, UserAlreadyExistsError, UpdatingUserError, InternalServerError, DeletingUserError


class UsersApi(Resource):

    def get(self):
        user = User.objects().to_json()
        return Response(user, mimetype="application/json", status=200)

    # reference to encrypt the password https://stackoverflow.com/questions/27943258/save-password-as-salted-hash-in-mongodb-in-users-collection-using-python-bcrypt
    # more info regarding bcrypt package -> https://pypi.org/project/bcrypt/

    def post(self):
        try:
            body = request.get_json()
            password_hash = generate_password_hash(body.get('password'))
            body['password'] = password_hash
            user = User(**body).save()
            id = user.id
            return {'msg': 'user is created successfully', 'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise UserAlreadyExistsError
        except Exception as err:
            raise InternalServerError


class UserAPI(Resource):
    def get(self, id):
        try:
            user = User.objects(id=id).to_json()
            return Response(user, mimetype="application/json", status=200)
        except DoesNotExist:
            raise UserNotExistsError
        except Exception as err:
            raise InternalServerError

    def put(self, id):
        try:
            body = request.get_json()
            User.objects.get(id=id).update(**body)
            return jsonify({
                "status": 200,
                "message": "Successfully update the user"
            })
        except DoesNotExist:
            raise UpdatingUserError
        except Exception as err:
            raise InternalServerError

    def delete(self, id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return jsonify({
                "status": 200,
                "message": "Successfully delete the user"
            })
        except DoesNotExist:
            raise DeletingUserError
        except Exception as err:
            raise InternalServerError
