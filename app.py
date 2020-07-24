from flask import Flask, request, make_response
from Controller.UserController import *
from Repository.UserRepositoryImp import *

app = Flask(__name__)

@app.route('/')
def hello():
    controller = UserController(request)
    return make_response(controller.ListUser(), 200)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')