""" has common methods used in all models"""
from .base import BaseModel 


class SalesModel(BaseModel):

    """
        sales model saved data in list 
        and has methods to manipulate it
    """

    def __init__(self):
        self.sales = []

    def get_sales(self):
        """
            get all the saved sale items
        """
        return self.sales

    def add_sales(self, data):
        """
            save items in list
        """
        self.sales.append(data)

    def calculate_total(self, price, quantity):
        """
            calculate the total of a sale
        """
        total = (price * quantity)
        return total

    def drop(self):
        """
         reset to empty list
        """

        self.sales.clear()

salesModel = SalesModel()
