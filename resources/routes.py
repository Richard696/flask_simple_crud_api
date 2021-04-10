from .user import UsersApi, UserAPI


def init_routes(api):
    api.add_resource(UsersApi, '/api/v1/user')
    api.add_resource(UserAPI, '/api/v1/user/<id>')
