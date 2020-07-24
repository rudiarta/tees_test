from flask import request
from Repository.UserRepositoryImp import *
from Repository.UserRepository import *
from Service.UserServiceImp import *
from Service.UserService import *

class UserController:
    def __init__(self, req: request):
        self.req = req
    
    def ListUser(self):
        repo: UserRepository = UserRepositoryImp()
        service: UserService = UserServiceImp(repo)
        return {"data":service.addUser()}