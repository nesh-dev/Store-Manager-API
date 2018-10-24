import psycopg2 
import os 
from psycopg2.extras import RealDictCursor

from flask import current_app
from app.bcrypt_instance import Bcrypt

# local imports
from .database_tables import list_of_tables, tables_to_drop

password = Bcrypt.generate_password_hash('123456').decode('utf-8')


def create_connection():
    """Create a database connection with the apps different config instances"""
    url = current_app.config.get('POSTGRES_DATABASE_URI')
    try:
        conn = psycopg2.connect(url)
        return conn
    except psycopg2.DatabaseError as e:
        return {'message': '{}'.format(e)}


def drop_all_tables():
    """drop all tables"""
    connection = create_connection()
    cursor = connection.cursor()
    for drop in tables_to_drop:
        cursor.execute(drop)
        connection.commit()
    connection.close()


def save_admin_test_user():
    """add the test admin user"""
    connection = create_connection()
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    try:
        query = """INSERT INTO users (user_name, email, password, role)
            values(%s, %s, %s, %s)"""
        cursor.execute(query, ('testadmin', 'testadmin@gmail.com', 
                               password, 2))
        connection.commit()
        data = cursor.fetchone()
        cursor.close()   
    except psycopg2.DatabaseError as e:
        return {'message': '{}'.format(e)}


def save_attendant_test_user():
    """add the test attendant user"""
    connection = create_connection()
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    try:
        query = """INSERT INTO users (user_name, email, password, role)
            values(%s, %s, %s, %s)"""
        cursor.execute(query, ('testattendant', 'testattendant@gmail.com', 
                               password, 1))
        connection.commit()
        data = cursor.fetchone()
        cursor.close()
    except psycopg2.DatabaseError as e:
        return {'message': '{}'.format(e)}


def all_test_data():
    save_attendant_test_user()
    save_admin_test_user()


def create_database_tables():
    """create tables"""
    connection = create_connection()
    cursor = connection.cursor()
    for table in list_of_tables:
        cursor.execute(table)
        connection.commit()
    connection.close()
    try:
        save_admin_test_user()
    except:
        pass