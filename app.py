from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:maulapor@127.0.0.1/maulapor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from controller.user.UserController import *
from controller.userdata.controller import *
from middleware.user.UserMiddleware import *

# route for user data
@app.route('/list-user-data', methods=['GET'])
@UserMiddleware
def userDataList():
    controller = UserController(request)
    return controller.ListUserData()

@app.route('/insert-user-data', methods=['POST'])
@UserMiddleware
def addUserData():
    controller = UserController(request)
    return controller.AddUserData()

@app.route('/update-user-data/<int:id>', methods=['PUT'])
@UserMiddleware
def updateUserData(id):
    controller = UserController(request)
    return controller.UpdateUserData(id)

@app.route('/delete-user-data/<int:id>', methods=['DELETE'])
@UserMiddleware
def deleteUserData(id):
    controller = UserController(request)
    return controller.DeleteUserData(id)

@app.route('/login', methods=['POST'])
def login():
    controller = UserDataController(request)
    return controller.login()

@app.route('/insert-user-profile', methods=['POST'])
@UserMiddleware
def addUserProfile():
    controller = UserDataController(request)
    return controller.addUserProfileData()


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)