class User:
    def __init__(self, userName, password, firstName:str = None, lastName:str = None, isActive:int = None):
        self.UserName = userName
        self.Password = password
        self.FirstName = firstName
        self.LastName = lastName
        self.IsActive = isActive