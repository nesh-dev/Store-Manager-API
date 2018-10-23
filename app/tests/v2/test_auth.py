
import json
from .dummy_data import users
from .base import BaseTest


class AuthEndpointsTestCase(BaseTest):
    """
    Tests for user auth
    """

    def test_register(self):
        """sucess register"""

        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(users[2]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('registration sucessfull', str(response.data))

    # test with empty_data data
    def test_register_without_data(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(users[4]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required parameter', str(response.data))

    # test already used email
    def test_register_existing_email(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(users[0]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 409)
        self.assertIn('user with email already registred', str(response.data))

    # test resgister invalid email
    def test_register_invalid_email(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(users[3]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)
        self.assertIn('invalid email', str(response.data))

    # test sucess login
    def test_login(self):
        response = self.client.post('/api/v2/auth/login', 
                                    data=json.dumps(users[0]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('logged in', str(response.data))

    # test login without data
    def test_login_without_data(self):
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(4),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required parameter ', str(response.data))

    # test login invalid email
    def test_login_invalid_password(self):
        response = self.client.post('/api/v2/auth/login', 
                                    data=json.dumps(users[5]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)
        self.assertIn('passwords do not match', str(response.data))

    # test login missing email
    def test_login_missing_email(self):
        response = self.client.post('/api/v2/auth/login', 
                                    data=json.dumps(users[6]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required parameter ', str(response.data))

    # test login missing password
    def test_login_missing_password(self):
        response = self.client.post('/api/v2/auth/login', 
                                    data=json.dumps(users[7]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        assert 'Missing required parameter ', str(response.data)

    # test login mismatching password
    def test_login_invalid_password(self):
        response = self.client.post('/api/v2/auth/login', 
                                    data=json.dumps(users[8]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)
        self.assertIn('username should not be empty', str(response.data))

    # test logout
    def test_logout(self):
        response = self.client.post('/api/v2/auth/logout',
                                    headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('logged out', str(response.data))

    # test logout already revoed token
    def test_logout(self):
        response = self.client.post('/api/v2/auth/logout',
                                    headers=self.attendant_headers)
        response = self.client.post('/api/v2/auth/logout',
                                    headers=self.attendant_headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn('token revoked', str(response.data))