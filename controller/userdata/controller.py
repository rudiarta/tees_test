from flask import request, make_response
from service.userdata.service import UserDataService
from service.userdata.serviceImp import UserDataServiceImp
from repository.userdata.repositoryImp import UserDataRepositoryImp
import pinject

class UserDataController:
    def __init__(self, req: request):
        self.req = req

    def login(self):
        username = self.req.form['username']
        password = self.req.form['password']

        obj = pinject.new_object_graph(binding_specs=[UserDataServiceBinding()])
        service: UserDataService = obj.provide(UserDataServiceImp)

        service.validateUser(username, password)

        return make_response({"status":"success"}, 200)

class UserDataServiceBinding(pinject.BindingSpec):
    def configure(self, bind):
        bind('repo', to_class=UserDataRepositoryImp)