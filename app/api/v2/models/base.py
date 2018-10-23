
from ..database.database_connection import create_connection


class BaseModel(object):
    """contains common functionality for the models"""

    def save_query(self, query):
        """save queries"""
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    def get_all(self, table):
        """method used to get all items in item"""
        query = "SELECT * FROM {}".format(table)
        self.save_query(query)

    def get_item(self, table, **kwargs):
        """method to get an item in table via key provided"""
        for key, val in kwargs.items():
            query = "SELECT * FROM {} WHERE {}={}".format(table, key, val)
            self.save_query(query)

    def delete(self, table, **kwargs):
        """method deletes items in db """
        for key, val in kwargs.items():
            query = "DELETE FROM {} WHERE {}={}".format(table, key, val)
            self.save_query(query)






