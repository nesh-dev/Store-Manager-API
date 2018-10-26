from psycopg2.extras import RealDictCursor
from .base import BaseModel 
from ..database.database_connection import create_connection


class CategoryModel(BaseModel):
    """ Model for categories """

    def __init__(self, name='prod', description='description'):
        self.name = name
        self.description = description
        self.connection = create_connection()
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def create_category(self):
        """method inserts in to category"""
        query = """ INSERT into categories (name, description) values('{}', '{}') 
         """.format(self.name, self.description)
        self.save_query(query)
        category = self.get_item('categories', name=self.name)
        category['created_at'] = str(category['created_at'])
        return category

    def update_category(self, id):
        """ update category field"""
        query = """UPDATE categories SET name='{}', description='{}'
        WHERE category_id = {}""".format(self.name, self.description, id)
        self.save_query(query)
        category = self.get_item('categories', category_id=id)
        if category is dict:
            category['created_at'] = str(category['created_at'])
            return category
        return category

    def add_products(self, category_id, product_id):
        """ add product to category """
        query = """INSERT into category_items(category_id, product_id) values('{}', '{}') 
         """.format(category_id, product_id)
        self.save_query(query)
        category = CategoryModel()
        category_obj = category.get_item('categories', category_id=category_id)
        if category_obj:
            category_name = category_obj['name']
        product_obj = category.get_item('products', product_id=product_id)
        if product_obj:
            product_name = product_obj['name']
        return {"product": product_name, "category": category_name}, 201
