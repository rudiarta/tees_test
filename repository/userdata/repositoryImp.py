from .repository import UserDataRepository
# from datamodel.user.UserProfileModel import UserProfile

import bcrypt

class UserDataRepositoryImp(UserDataRepository):
    def validateUser(self, username, password) -> str:
        userData = UserProfile.query.filter_by(username=username, password=password).first()
        print(userData is None)
        print("oke")