from .base import BaseModel
"""
    user model
    Dictionary data is saved in a list
"""


class UserModel(BaseModel):

    # initialize
    def __init__(self):
        self.users = []
        self.blacklist_list = []

    def get_users(self):
        return self.users

    # append user to the list
    def add_user(self, data):
        self.users.append(data)

    def get_by_name(self, name, data):
        for item in data:
            if item['email'] == name:
                return item

    # add the blacklisted tokens
    def blacklist(self, data):
        self.blacklist_list.append(data)

    # check if the token
    def check_if_blacklist(self, data):
        if data in self.blacklist_list:
            return True
        return False

    # required for clearing the data
    def drop(self):
        self.users.clear()

UserModel = UserModel()
