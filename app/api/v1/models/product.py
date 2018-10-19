from .base import BaseModel
"""
    Product Model 

"""


class ProductModel(BaseModel):

    def __init__(self):
        self.products = []

    def get_products(self):
        return self.products

    def add_product(self, data):
        self.products.append(data)

    # reset to empty list
    def drop(self):
        self.products.clear()

ProductModel = ProductModel()
