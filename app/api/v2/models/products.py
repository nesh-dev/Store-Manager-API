
from psycopg2.extras import RealDictCursor
from .base import BaseModel 
from ..database.database_connection import create_connection


class ProductsModel(BaseModel):
    """ Model for products """

    MINIMUM_INVENTORY = 100

    def __init__(self, name='prod', price=0, description='desc', quantity=0):
        self.name = name
        self.price = price 
        self.description = description
        self.quantity = quantity
        self.minimum_inventory = ProductsModel.MINIMUM_INVENTORY
        self.connection = create_connection()
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def create_product(self):
        """ insert products data in the products table """
        query = """ INSERT into products (name, description,
         quantity, minimum_inventory, price) values('{}', '{}', '{}', '{}',
        '{}') 
         """.format(self.name, self.description, 
                    self.quantity, self.minimum_inventory, self.price)
        self.save_query(query)
        product = self.get_item('products', name=self.name)
        product['created_at'] = str(product['created_at'])
        return product
        
    def update_products(self, id, name, price, description, quantity,
                        minimum_inventory):
        """update products """
        
        query = """UPDATE products SET name='{}', description='{}', 
        quantity='{}', minimum_inventory='{}',
            price='{}' WHERE product_id='{}'
            """.format(name, description, 
                       quantity, minimum_inventory, price, 
                       id)
        self.save_query(query)
        product = self.get_item('products', product_id=id)
        if type(product) == dict:
            product['created_at'] = str(product['created_at'])
            return product
        return product