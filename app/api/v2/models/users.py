from .base import BaseModel 


class UserModel(BaseModel):
    """ UserModel to handle authentication """
    ADMIN = 2
    ATTENDANT = 1

    def __init__(self, user_name, email, password, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = ATTENDANT

    def create_user(self):
        query = """ INSERT into users (user_name, email,
         password, role) values({}, {}, {}, {}) 
         """.format(self.username, self.email, self.password, 
                    self.role)
        self.save_query(query)

    

