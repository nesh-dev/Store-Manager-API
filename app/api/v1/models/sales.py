
from .base import BaseModel 


class SalesModel(BaseModel):

    def __init__(self):
        self.sales = []

    def get_sales(self):
        return self.sales

    def add_sales(self, data):
        self.sales.append(data)

    def calculate_total(self, price, quantity):
        total = (price * quantity)
        return total

    # reset to empty list
    def drop(self):
        self.sales.clear()

SalesModel = SalesModel()
