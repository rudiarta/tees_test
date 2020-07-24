from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from controller.user.UserController import *
from middleware.user.UserMiddleware import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:maulapor@127.0.0.1/maulapor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/user-list', methods=['GET'])
def userDataList():
    controller = UserController(request)
    return controller.ListUserData()

@app.route('/insert-user', methods=['POST'])
@UserMiddleware
def addUserData():
    controller = UserController(request)
    return controller.AddUserData()

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')