from .base import BaseModel

"""
Category Model

"""


class CategoryModel(BaseModel):

    def __init__(self):
        self.category = []

    # get all orders
    def get_categories(self):
        return self.category

    # add a category in list
    def add_category(self, data):
        return self.category.append(data)

    # reset to empty list
    def drop(self):
        self.category.clear() 
        print(self.category)

CategoryModel = CategoryModel()
