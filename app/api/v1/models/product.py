from .base import BaseModel 


class ProductModel(BaseModel):

    def __init__(self):
        self.products = []

    def get_products(self):
        return self.products

    def add_product(self, data):
        self.products.append(data)


ProductModel = ProductModel()