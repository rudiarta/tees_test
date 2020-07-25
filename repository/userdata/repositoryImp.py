from .repository import UserDataRepository
from datamodel.user.UserProfileModel import UserProfile
from app import db

import bcrypt

class UserDataRepositoryImp(UserDataRepository):
    def validateUser(self, username, password) -> dict:
        
        userData = UserProfile.query.filter_by(username=username).first()
        if userData is not None:
            bytePassword = bytes(userData.password, 'ascii')
            if bcrypt.checkpw(password, bytePassword):
               return {"id":userData.id,"username":userData.username,"status":"success"}
        
        return {"status":"failed"}

    def addUser(self, name, username, password, profilePicture) -> bool:
        try:
            userData = UserProfile(name, username, password, profilePicture)
            db.session.add(userData)
            db.session.commit()
            return True
        except:
            return False
        