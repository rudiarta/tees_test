from .service import UserDataService
from repository.userdata.repository import UserDataRepository
import jwt
import datetime
import os
import bcrypt

class UserDataServiceImp(UserDataService):

    def __init__(self, repo: UserDataRepository):
        self.repo = repo

    def validateUser(self, username, password) -> str:
        bytePassword = bytes(password, 'ascii')
        
        data = self.repo.validateUser(username, bytePassword)
        if data['status'] == 'failed':
            raise Exception("error")

        data['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        
        token = jwt.encode(data,"secret")
        strToken = str(token, 'ascii')
        return strToken

    def addUser(self, name, username, password, profilePicture) -> bool:
        path = "gambar/"
        try:
            os.mkdir(path)
        except OSError:
            pass

        filePath = 'gambar/'+profilePicture.filename
        profilePicture.save(filePath)

        passwd = bytes(password, 'ascii')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(passwd, salt)
        pw = str(hashed, 'ascii')

        if self.repo.addUser(name, username, pw, profilePicture.filename) is not True:
            os.remove(filePath)
            return False
        return True