from flask import Flask
from flask_cors import CORS
# from flask_bcrypt import Bcrypt

# Self define library function
from config.conf import dbURI
from database.db import initializeDB
from resources.user import users

app = Flask(__name__)
CORS(app)  # allow cross origin request
# bcrypt = Bcrypt(app)
# connect the application to mongodb
app.config['MONGO_SETTINGS'] = {'host': dbURI}
initializeDB(app)
app.register_blueprint(users)

if __name__ == '__main__':
    app.run(debug=True)
