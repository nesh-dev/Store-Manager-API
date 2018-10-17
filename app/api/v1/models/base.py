

class BaseModel(object):

    # get item by id
    def get_by_id(self, id, data):
        for item in data:
            if item['id'] == id:
                return item

    # get item by name
    def get_by_name(self, name, data):
        for item in data:
            if item['name'] == name:
                return item

    # delete item from list 
    def delete(self, id, data):
        item = self.get_by_id(id, data)
        return data.remove(item)

    def get_length(self, data):
        length = len(data)
        return length


