from Repository.UserRepository import *

class UserRepositoryImp(UserRepository):
    def __init__(self):
        pass
    
    def Insert(self) -> str:
        return "insert imp from repo"