from .base import BaseModel
"""
    user model
    Dictionary data is saved in a list
"""


class UserModel(BaseModel):
    def __init__(self):
        self.users = []
        self.blacklist_list = []

    def get_users(self):
        return self.users

    def add_user(self, data):
        self.users.append(data)

    def get_by_name(self, name, data):
        for item in data:
            if item['email'] == name:
                return item

    def blacklist(self, data):
        self.blacklist_list.append(data)

    def check_if_blacklist(self, data):
        if data in self.blacklist_list:
            return True
        return False

    def drop(self):
        self.users.clear()

UserModel = UserModel()
