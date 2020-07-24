from repository.user.UserRepository import UserRepository
from datamodel.user.UserDataModel import UserData

class UserRepositoryImp(UserRepository):
    def __init__(self):
        pass
    
    def getUser(self):
        userDatas = UserData.query.all()        
        return userDatas