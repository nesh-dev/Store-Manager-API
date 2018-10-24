
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
                                    headers=self.admin_headers,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('registration sucessfull', str(response.data))

    def test_register_without_data(self):
        """test with empty_data data"""
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(users[4]),
                                    headers=self.admin_headers,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required parameter', str(response.data))

    def test_register_existing_email(self):
        """test already used email"""
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(users[0]),
                                    headers=self.admin_headers,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 409)
        self.assertIn('user with email already registred', str(response.data))

    def test_register_invalid_email(self):
        """test resgister invalid email"""
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(users[3]),
                                    headers=self.admin_headers,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)
        self.assertIn('invalid email', str(response.data))

    def test_login(self):
        """  test sucess login"""
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(users[0]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('logged in', str(response.data))

    def test_login_invalid_password(self):
        """test login invalid email"""
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(users[5]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)
        self.assertIn('invalid credentials', str(response.data))

    def test_login_missing_email(self):
        """# test login missing email"""
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(users[6]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required parameter ', str(response.data))

    def test_login_missing_password(self):
        """ test login missing password """
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(users[7]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        assert 'Missing required parameter ', str(response.data)

    def test_login_empty_field(self):
        """test login mismatching password"""
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(users[8]),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)
        self.assertIn('invalid credentials', str(response.data))

    def test_logout(self):
        """# test logout"""
        response = self.client.post('/api/v2/auth/logout',
                                    headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('logged out', str(response.data))

    def test_logout_revoked(self):
        """test logout already revoed token"""
        response = self.client.post('/api/v2/auth/logout',
                                    headers=self.attendant_headers)
        response = self.client.post('/api/v2/auth/logout',
                                    headers=self.attendant_headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn('Token has been revoked', str(response.data))
