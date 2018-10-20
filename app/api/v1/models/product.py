
""" get common methods by inheriting from basemodel"""
from .base import BaseModel


class ProductModel(BaseModel):

    """
        Product model manipulates item stored in list
    """

    def __init__(self):
        self.products = []

    def get_products(self):
        """
            return all elements in list
        """
        return self.products

    def add_product(self, data):
        """
            append produt items to list
        """
        self.products.append(data)

    # reset to empty list
    def drop(self):
        """
            clear all list items used for tearDown in tests
        """
        self.products.clear()


# create an instace of the class
productModel = ProductModel()

