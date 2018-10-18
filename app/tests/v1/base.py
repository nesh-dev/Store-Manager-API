import unittest 
import json
from ... import create_app

from .dummy import users, empty, category


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()

        # to handle error in tests
        self.client.post('api/v1/register', data=json.dumps(users[8]),
                         content_type='application/json')
        user = self.client.post('api/v1/login', data=json.dumps(users[8]),
                                content_type='application/json')
        attendant_token = user.get_json().get('access_token')

        # handle error in tests
        self.client.post('api/v1/register', data=json.dumps(users[0]),
                         content_type='application/json')
        user = self.client.post('api/v1/login', data=json.dumps(users[0]),
                                content_type='application/json')
        admin_token = user.get_json().get('access_token')

        self.admin_headers = admin_headers = {
            'Authorization': 'Bearer {}'.format(admin_token),
            'Content-Type': 'application/json'}

        self.attendant_headers = {
            'Authorization': 'Bearer {}'.format(attendant_token),
            'Content-Type': 'application/json'
            }

        # create a test category 
        self.client.post('/api/v1/categories',
                         data=json.dumps(category[0]),
                         content_type='application/json',
                         headers=self.admin_headers)
        