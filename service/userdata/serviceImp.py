from .service import UserDataService
from repository.userdata.repository import UserDataRepository
import bcrypt
from app import db

class UserDataServiceImp(UserDataService):

    def __init__(self, repo: UserDataRepository):
        self.repo = repo

    def validateUser(self, username, password) -> str:
        bytePassword = bytes(password, 'ascii')
        bcryptPassword = bcrypt.hashpw(bytePassword, bcrypt.gensalt())
        
        self.repo.validateUser(username, bcryptPassword)