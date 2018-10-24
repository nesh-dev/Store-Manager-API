import psycopg2 
import os 
from flask import current_app
from app.bcrypt_instance import Bcrypt

# local imports
from .database_tables import list_of_tables, tables_to_drop


def create_connection():
    """Create a database connection with the apps different config instances"""
    url = current_app.config.get('POSTGRES_DATABASE_URI')
    try:
        conn = psycopg2.connect(url)
        return conn
    except psycopg2.DatabaseError as e:
        return {'message': '{}'.format(e)}


def create_database_tables():
    """create tables"""
    connection = create_connection()
    cursor = connection.cursor()
    for table in list_of_tables:
        cursor.execute(table)
        connection.commit()


def drop_all_tables():
    """drop all tables"""
    connection = create_connection()
    cursor = connection.cursor()
    for drop in tables_to_drop:
        cursor.execute(drop)
        connection.commit()
