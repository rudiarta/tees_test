import unittest
from service.user.UserServiceImp import UserServiceImp
from repository.user.UserRepository import UserRepository

class ServiceTest(unittest.TestCase):

    def test_add_user_false(self):
        repo = MockUserRepository()
        service = UserServiceImp(repo)
        result = service.addUser("a", "a", 2)
        self.assertEqual(result, False)
    def test_add_user_true(self):
        repo = MockUserRepository()
        service = UserServiceImp(repo)
        result = service.addUser("b", "a", 2)
        self.assertEqual(result, True)
    def test_delete_user_true(self):
        repo = MockUserRepository()
        service = UserServiceImp(repo)
        self.assertEqual(service.deleteUser(2), True)
    def test_delete_user_false(self):
        repo = MockUserRepository()
        service = UserServiceImp(repo)
        self.assertEqual(service.deleteUser(1), False)
    def test_update_user_true(self):
        repo = MockUserRepository()
        service = UserServiceImp(repo)
        self.assertEqual(service.updateUser(2, "b", "a", 2), True)
    def test_update_user_false(self):
        repo = MockUserRepository()
        service = UserServiceImp(repo)
        self.assertEqual(service.updateUser(1, "b", "a", 2), False)

class MockUserRepository(UserRepository):
    def addUser(self, name, email, shirtSize):
        if name == "a":
            raise Exception("Error")
        return True
    def deleteUser(self, id):
        if id == 1:
            raise Exception("Error")
        return True
    def updateUser(self, id, name, email, shirtSize):
        if id == 1:
            raise AttributeError("Error")
        return True
    def getUser(self):     
        return ["userDatas"]
