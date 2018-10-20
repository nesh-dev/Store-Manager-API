

class BaseModel(object):

    """
       Base Model has common methods 

    """

    def get_by_id(self, id, data):
        """
            get item by id
        """
        for item in data:
            if item['id'] == id:
                return item

    def get_by_name(self, name, data):
        """
            get item in dictionary by name
        """
        for item in data:
            if item['name'] == name:
                return item

    def delete(self, id, data):
        """
            delete item in dictionary
        """

        item = self.get_by_id(id, data)
        return data.remove(item)

    def get_length(self, data):
        """
            get the length of the data argmunt
        """
        length = len(data)
        return length
        
