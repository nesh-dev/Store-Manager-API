"""contains the common methods """
from .base import BaseModel
from ..database.database_connection import create_connection
from psycopg2.extras import RealDictCursor


class Blacklisted(BaseModel):
    """model handles blacklisted tokens """

    def __init__(self, blacklist):
        self.blacklist = blacklist
        self.connection = create_connection()
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def blacklisted(self):
        """ insert into blacklist table """
        query = """ INSERT into blacklisted (token)
            values('{}')""".format(self.blacklist)
        self.save_query(query)

    def check_if_blacklist(self):
        """ check if the token has been blacklisted """
        response = None
        query = """SELECT * FROM blacklisted where token ='{}' 
                """.format(self.blacklist)
        self.cursor.execute(query)
        self.connection.commit()
        response = self.cursor.fetchall()
        if response is None:
            return False
        return True

