from repository.user.UserRepository import UserRepository
from service.user.UserService import UserService
import json

class UserServiceImp(UserService):
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def getUser(self): 
        start =  '{"data":['
        i = 1
        for data in self.repo.getUser():
            tmp = {
                "name": data.name,
                "email": data.email,
                "shirt_size": data.shirt_size
            }
            convert = json.dumps(tmp)
            if i != len(self.repo.getUser()):
                start = start + convert + ","
            else:
                start = start + convert
            i = i + 1

        end = ']}'

        # parse start:
        end = json.loads(start+end)

        return end
