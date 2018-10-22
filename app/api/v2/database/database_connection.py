import psycopg2 
import os 
from flask import current_app


def create_conn():
    """Create a database connection with the apps different config instances"""
    url = current_app.config.get('POSTGRES_DATABASE_URI')
    try:
        conn = psycopg2.connect(url)
        return conn
    except psycopg2.DatabaseError as e:
        return {'message': '{}'.format(e)}