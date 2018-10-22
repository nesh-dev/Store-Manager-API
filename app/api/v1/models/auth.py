"""
    contains common methods used in models
"""

from .base import BaseModel


class UserModel(BaseModel):

    """
    user model
    Dictionary data is saved in a list
    """

    # initialize
    def __init__(self):
        self.users = []
        self.blacklist_list = []

    def get_users(self):
        """
            return all user items
        """
        return self.users

    def add_user(self, data):
        """
         append user to the list
        """

        self.users.append(data)

    def get_by_name(self, name, data):
        """
            get an item in dictionary by name
        """
        for item in data:
            if item['email'] == name:
                return item

    def blacklist(self, data):
        """
             add the blacklisted tokens
        """
        self.blacklist_list.append(data)

    def check_if_blacklist(self, data):
        """
            check if the token is in blacklist
        """
        if data in self.blacklist_list:
            return True
        return False

    def drop(self):
        """
            required for clearing the data after tests
        """
        self.users.clear()


userModel = UserModel()


