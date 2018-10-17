

class BaseModel(object):

    def get_by_id(self, id, data):
        for item in data:
            if item['id'] == id:
                return item

    def get_by_name(self, name, data):
        for item in data:
            if item['name'] == name:
                return item

    def delete(self, id, data):
        item = self.get_by_id(id, data)
        return data.remove(item)

    def get_length(self, data):
        length = len(data)
        return length


