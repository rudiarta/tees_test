from repository.user.UserRepository import UserRepository
from service.user.UserService import UserService

class UserServiceImp(UserService):
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def addUser(self) -> str: 
        return self.repo.Insert()
