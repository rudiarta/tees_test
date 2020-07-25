from repository.user.UserRepository import UserRepository
from datamodel.user.UserDataModel import UserData
from app import db

class UserRepositoryImp(UserRepository):
    def __init__(self):
        pass
    
    def getUser(self):
        userDatas = UserData.query.all()        
        return userDatas

    def addUser(self, name, email, shirtSize): 
        userData = UserData(name, email, shirtSize)
        db.session.add(userData)
        db.session.commit()