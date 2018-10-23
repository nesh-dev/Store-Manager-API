from .base import BaseModel
from ..database.database_connection import create_connection
from psycopg2.extras import RealDictCursor


class Blacklisted(BaseModel):
    """model handles blacklisted tokens """
    def __init__(self, blacklist):
        self.blacklist = blacklist 

    def blacklisted(self):
        """ insert into blacklist table """
        query = """ INSERT into blacklisted (token)
            value({})""".format(self.blacklist)
        self.save_query(query)

    def check_if_blacklist(self):
        connection, response = create_connection(), None
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        query = """SELECT * FROM blacklisted where token ={} 
                """.format(self.blacklist)
        cursor.execute(query)
        connection.commit()
        response = cursor.fetechall()
        if len(response) > 0:
            return False
        return True

