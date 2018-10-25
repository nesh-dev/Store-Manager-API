""""add unittest as testing framework"""
import unittest
import json
from .dummy_data import users, sale_items, products
from ... import create_app
from ...api.v2.database.database_connection import (create_database_tables,
                                                    drop_all_tables, 
                                                    all_test_data)


class BaseTest(unittest.TestCase):
    """ Base test for other test cases to inherit """

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()

        with self.app.app_context():
            create_database_tables()
            all_test_data()

        # get admin tokens
        self.client.post('/api/v2/auth/signup', json=users[0])
        response = self.client.post('/api/v2/auth/login', json=users[0])
        if response:
            admin_token = response.get_json().get('access_token')
        self.admin_headers = {
            'Authorization': 'Bearer {}'.format(admin_token),
            'Content-Type': 'application/json'
        }

        # get user tokens
        self.client.post('/api/v2/auth/signup', json=users[1])
        response = self.client.post('api/v2/auth/login', json=users[1])
        if response:
            user_token = response.get_json().get('access_token')
            self.attendant_headers = {
                'Authorization': 'Bearer {}'.format(user_token),
                'Content-Type': 'application/json'}

        self.client.post('/api/v2/products', data=json.dumps(products[0]),
                         content_type='application/json',
                         headers=self.admin_headers)
        self.client.post('/api/v2/sales', data=json.dumps(sale_items[0]),
                         content_type='application/json',
                         headers=self.attendant_headers)

    def tearDown(self):
        """teardown all the test data"""
        with self.app.app_context():
            drop_all_tables()
