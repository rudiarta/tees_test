from .repository import UserDataRepository
from datamodel.user.UserProfileModel import UserProfile

import bcrypt

class UserDataRepositoryImp(UserDataRepository):
    def validateUser(self, username, password) -> dict:
        
        userData = UserProfile.query.filter_by(username=username).first()
        if userData is not None:
            bytePassword = bytes(userData.password, 'ascii')
            if bcrypt.checkpw(password, bytePassword):
               return {"id":userData.id,"username":userData.username,"status":"success"}
        
        return {"status":"failed"}
        