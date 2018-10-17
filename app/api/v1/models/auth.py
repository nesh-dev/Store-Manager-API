from .base import BaseModel


class UserModel(BaseModel):
    def __init__(self):
        self.users = []

    def get_users(self):
        return self.users

    def add_user(self, data):
        self.users.append(data)


UserModel = UserModel()
