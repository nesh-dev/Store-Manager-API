
from psycopg2.extras import RealDictCursor
from .base import BaseModel 
from ..database.database_connection import create_connection

class UserModel(BaseModel):
    """ UserModel to handle authentication """
    admin = 2
    attendant = 1

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.role = 1
        self.connection = create_connection()
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

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
