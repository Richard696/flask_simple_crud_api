from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_bcrypt import Bcrypt
from resources.routes import init_routes
from resources.error import errors

# Self define library function
from config.conf import dbURI
from database.db import initializeDB


app = Flask(__name__)
CORS(app)  # allow cross origin request
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)

# connect the application to mongodb
app.config['MONGO_SETTINGS'] = {'host': dbURI}

initializeDB(app)
init_routes(api)

if __name__ == '__main__':
    app.run(debug=True)  # currently run in debug mode
