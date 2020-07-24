from flask import request, make_response
from repository.user.UserRepositoryImp import UserRepositoryImp
from repository.user.UserRepository import UserRepository
from service.user.UserServiceImp import UserServiceImp
from service.user.UserService import UserService

class UserController:
    def __init__(self, req: request):
        self.req = req
    
    def ListUser(self):
        repo: UserRepository = UserRepositoryImp()
        service: UserService = UserServiceImp(repo)
        return make_response( {"data":service.addUser()}, 200)
