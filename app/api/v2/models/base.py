
from ..database.database_connection import create_connection
from psycopg2.extras import RealDictCursor


class BaseModel(object):
    """contains common functionality for the models"""
    def __init__(self):
        self.connection = create_connection()
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def save_query(self, query):
        """save queries"""
        self.cursor.execute(query)
        self.connection.commit()
    
    def get_all(self, table):
        """method used to get all items in item"""
        query = "SELECT * FROM {}".format(table)
        self.save_query(query)
        all_items = self.cursor.fetchall()
        if not all_items:
            return {"message": "no saved products"}, 404
        for item in all_items:
            string_date = {'created_at': str(item['created_at'])}
            item.update(string_date) 
        return all_items

    def get_item(self, table, **kwargs):
        """method to get an item in table via key provided"""
        for key, val in kwargs.items():
            query = """SELECT * FROM {} WHERE {}='{}';
            """.format(table, key, val)
            self.save_query(query)
            item = self.cursor.fetchone()
            if item is None:
                return {"message": "item {} does not exist".format(key)}, 404
            item['created_at'] = str(item['created_at'])
            return item

    def delete(self, table, **kwargs):
        """method deletes items in db """
        for key, val in kwargs.items():
            query = "DELETE FROM {} WHERE {}={}".format(table, key, val)
            self.save_query(query)






