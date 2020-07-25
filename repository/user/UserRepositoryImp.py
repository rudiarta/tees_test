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

    def updateUser(self, id, name, email, shirtSize):
        userData = UserData.query.get(id)
        userData.name = name
        userData.email = email
        userData.shirt_size = shirtSize
        db.session.commit()
    
    def deleteUser(self, id):
        userData = UserData.query.get(id)
        db.session.delete(userData)
        db.session.commit()