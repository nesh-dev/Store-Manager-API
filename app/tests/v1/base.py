import unittest 
import json
from ... import create_app

from .dummy import users, empty


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()

        # to handle error in tests
        self.client.post('api/v1/register', json.dumps(users[8]))
        user = self.client.post('api/v1/login', json.dumps(users[8]))
        attendant_token = ""
        # attendant_token = user.get_json().get('access_token')

        # handle error in tests
        self.client.post('api/v1/register', json.dumps(users[0]))
        user = self.client.post('api/v1/login', json.dumps(users[0]))
        admin_token = ""
        # admin_token = user.get_json().get('access_token')

        self.admin_headers = admin_headers = {
            'Authorization': 'Bearer {}'.format(admin_token),
            'Content-Type': 'application/json'}

        self.attendant_headers = {
            'Authorization': 'Bearer {}'.format(attendant_token),
            'Content-Type': 'application/json'
            }

        