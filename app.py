from flask import Flask, request, make_response
from controller.user.UserController import UserController
from middleware.user.UserMiddleware import UserMiddleware

app = Flask(__name__)

@app.route('/')
@UserMiddleware
def userList():
    controller = UserController(request)
    return controller.ListUser()

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')