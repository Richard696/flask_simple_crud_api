from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def hello():
    return {'msg': "Hello, World"}

@app.route('/v1/user', methods=['POST'])
def add_user():
    user = request.get_json()



if __name__ == '__main__':
    app.run(debug=True)