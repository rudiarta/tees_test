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

        try:
            token = service.validateUser(username, password)
        except:
            return make_response({"status":"failed"}, 401)

        return make_response({"status":"success","token":token}, 200)

    def addUserProfileData(self):
        name = self.req.form['name']
        username = self.req.form['username']
        password = self.req.form['password']
        profilePicture = self.req.files['profile_picture']

        obj = pinject.new_object_graph(binding_specs=[UserDataServiceBinding()])
        service: UserDataService = obj.provide(UserDataServiceImp)

        if service.addUser(name, username, password, profilePicture):
            return make_response({"status":"success"}, 200)
        return make_response({"status":"failed"}, 422)

class UserDataServiceBinding(pinject.BindingSpec):
    def configure(self, bind):
        bind('repo', to_class=UserDataRepositoryImp)