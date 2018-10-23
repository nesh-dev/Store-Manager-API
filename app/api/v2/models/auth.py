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
        """ insert user data in the users table """
        query = """ INSERT into users (user_name, email,
         password, role) values('{}', '{}', '{}', '{}') 
         """.format(self.username, self.email, self.password, 
                    self.role)
        self.save_query(query)

    def change_role(self, id):
        query = """ UPDATE  users SET role='{}' WHERE user_id='{}' 
        """.format(self.role, id)
        self.save_query(query)
