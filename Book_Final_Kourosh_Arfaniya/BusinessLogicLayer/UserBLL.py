from DataAccessLayer.UserDAL import UserDALClass
from Model.UserModel import User







class UserBLL:
    def getUserbyUserNamePassword(self, userObject:User):
        userDALObject = UserDALClass()
        return userDALObject.getUserbyUserNamePassword(userObject)