import sqlite3
from Model.UserModel import User




class UserDALClass:
    def getUserbyUserNamePassword(self,userObject:User):
        connectionString = 'DB/databasefolder.db'
        commandText = 'select UserName,Password,FirstName,LastName,isActive from User where UserName=? and Password=?'

        params = (userObject.UserName, userObject.Password)
        with sqlite3.connect(connectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandText,params)
            row = cursor.fetchall()
        return row







