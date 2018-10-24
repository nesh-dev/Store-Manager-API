
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
        return all_items

    def get_item(self, table, **kwargs):
        """method to get an item in table via key provided"""
        for key, val in kwargs.items():
            query = """SELECT * FROM {} WHERE {}='{}';
            """.format(table, key, val)
            self.save_query(query)
            item = self.cursor.fetchone()
            return item

    def delete(self, table, **kwargs):
        """method deletes items in db """
        for key, val in kwargs.items():
            query = "DELETE FROM {} WHERE {}={}".format(table, key, val)
            self.save_query(query)






