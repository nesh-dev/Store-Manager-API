from .base import BaseModel


class UserModel(BaseModel):
    def __init__(self):
        self.users = []

    def get_users(self):
        return self.users

    def add_user(self, data):
        self.users.append(data)

    def get_by_name(self, name, data):
        for item in data:
            if item['email'] == name:
                return item


UserModel = UserModel()
