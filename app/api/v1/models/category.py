
""" inherits common methods """
from .base import BaseModel


class Categorymodel(BaseModel):

    """
        Category Model has saved data

    """

    def __init__(self):
        self.category = []

    def get_categories(self):
        """
            get all categories
        """
        return self.category

    def add_category(self, data):
        """
            add category items
        """
        return self.category.append(data)

    def drop(self):
        """
            used in tests to clear data in categories
        """
        self.category.clear()
        print(self.category)


categoryModel = Categorymodel()
