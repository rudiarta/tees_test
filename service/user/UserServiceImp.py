from repository.user.UserRepository import UserRepository
from service.user.UserService import UserService
import json

class UserServiceImp(UserService):
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def getUser(self): 
        start =  '{"status":"success","data":['
        i = 1
        for data in self.repo.getUser():
            tmp = {
                "id": data.id,
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
        result = json.loads(start+end)
        return result

    def addUser(self, name, email, shirtSize) -> bool:
        try:
            self.repo.addUser(name, email, shirtSize)
            return True
        except:
            return False

    def updateUser(self, id, name, email, shirtSize) -> bool:
        try:
            self.repo.updateUser(id, name, email, shirtSize)
            return True
        except AttributeError as e:
            return False
    
    def deleteUser(self, id) -> bool:
        try:
            self.repo.deleteUser(id)
            return True
        except:
            return False
