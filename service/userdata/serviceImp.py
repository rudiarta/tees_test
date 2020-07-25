from .service import UserDataService
from repository.userdata.repository import UserDataRepository
import jwt
import datetime

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