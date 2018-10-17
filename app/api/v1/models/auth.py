

class UserModel():
    def __init__(self):
        self.users = []

    def get_users(self):
        return self.users

    def add_user(self, data):
        self.users.append(data)

    def get_by_id(self, id, data):
        for item in data:
            if item['id'] == id:
                return item

    def get_by_name(self, name, data):
        for item in data:
            if item['name'] == name:
                return item
    
    