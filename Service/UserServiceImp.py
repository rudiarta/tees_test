from Repository.UserRepository import *
from Service.UserService import *

class UserServiceImp(UserService):
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def addUser(self) -> str: 
        return self.repo.Insert()
