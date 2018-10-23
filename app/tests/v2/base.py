""""add unittest as testing framework"""
import unittest

from .dummy_data import users
from ... import create_app


class BaseTest(unittest.TestCase):
    """ Base test for other test cases to inherit """

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()

        # get admin tokens 
        self.client.post('/api/v2/auth/signup', json=users[0])
        response = self.client.post('/api/v2/auth/login', json=users[0])
        if response:
            # admin_token = response.get_json().get('access_token')
            admin_token = ''
        self.admin_headers = {
            'Authorization': 'Bearer {}'.format(admin_token),
            'Content-Type': 'application/json'
        }

        # get user tokens
        self.client.post('/api/v2/auth/signup', json=users[1])
        response = self.client.post('api/v2/auth/login', json=users[1])
        if response:
            # user_token = response.get_json().get('access_token')
            user_token = ""
            self.attendant_headers = {
                'Authorization': 'Bearer {}'.format(user_token),
                'Content-Type': 'application/json'}

        def tearDown(self):
            """teardown all the test data"""
            pass
