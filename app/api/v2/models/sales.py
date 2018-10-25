
from psycopg2.extras import RealDictCursor
from .base import BaseModel 
from ..database.database_connection import create_connection


class SalesModel(BaseModel):
    """ Model for products """

    def __init__(self, customer='name', total=0, quantity=0):
        self.customer = customer
        self.total = total
        self.quantity = quantity
        self.connection = create_connection()
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def create_sale(self, attendant, product_id, iteration):
        """ insert sales data in the sales table """
        query = """ INSERT into sales (attendant_email, customer, total) 
        values('{}', '{}', '{}') RETURNING sale_id

         """.format(attendant, self.customer, self.total)
        connection = create_connection()
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query)
        connection.commit()
        sale_id = cursor.fetchone()['sale_id']

        for i in range(iteration):
            sale_items_query = """ INSERT into sale_items (sale_id, product_id,
             quantity) values('{}', '{}', '{}')
            
             """.format(sale_id, product_id, 
                        self.quantity)

            self.save_query(sale_items_query)

        
    # def update_products(self, id, name, price, description, quantity,
    #                     minimum_inventory):
    #     """update products """
        
    #     query = """UPDATE products SET name='{}', description='{}', 
    #     quantity='{}', minimum_inventory='{}',
    #         price='{}' WHERE product_id='{}'
    #         """.format(name, description, 
    #                    quantity, minimum_inventory, price, 
    #                    id)
    #     self.save_query(query)
    #     product = self.get_item('products', product_id=id)
    #     if type(product) == dict:
    #         product['created_at'] = str(product['created_at'])
    #         return product
    #     return product