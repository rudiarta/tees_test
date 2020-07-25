from flask import request, make_response
import json
from repository.user.UserRepositoryImp import UserRepositoryImp
from repository.user.UserRepository import UserRepository
from service.user.UserServiceImp import UserServiceImp
from service.user.UserService import UserService
import pinject

class UserController:
    def __init__(self, req: request):
        self.req = req
    
    def ListUserData(self):
        obj_graph = pinject.new_object_graph(binding_specs=[UserServiceBindingSpec()])
        service: UserService = obj_graph.provide(UserServiceImp)
        
        return make_response( service.getUser(), 200)

    def AddUserData(self):

        name = self.req.form['name']
        email = self.req.form['email']
        shirtSize = self.req.form['shirt_size']

        obj_graph = pinject.new_object_graph(binding_specs=[UserServiceBindingSpec()])
        service: UserService = obj_graph.provide(UserServiceImp)
        
        if  service.addUser(name, email, shirtSize):
            return make_response( {"status":"success"}, 200)
        
        return make_response( {"status":"failed"}, 422)

    def UpdateUserData(self, id):

        name = self.req.form['name']
        email = self.req.form['email']
        shirtSize = self.req.form['shirt_size']
        
        obj_graph = pinject.new_object_graph(binding_specs=[UserServiceBindingSpec()])
        service: UserService = obj_graph.provide(UserServiceImp)

        if service.updateUser(id, name, email, shirtSize):
            return make_response( {"status":"success"}, 200)
        
        return make_response( {"status":"failed"}, 422)

    def DeleteUserData(self, id):
        obj_graph = pinject.new_object_graph(binding_specs=[UserServiceBindingSpec()])
        service: UserService = obj_graph.provide(UserServiceImp)

        if service.deleteUser(id):
            return make_response( {"status":"success"}, 200)
        
        return make_response( {"status":"failed"}, 422)

class UserServiceBindingSpec(pinject.BindingSpec):
     def configure(self, bind):
         bind('repo', to_class=UserRepositoryImp)
