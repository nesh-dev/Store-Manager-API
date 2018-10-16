import unittest

from .dummy import users, empty
from .base import BaseTest
"""
    Tests for user auth
"""


class AuthEndpointsTestCase(BaseTest):

    # sucess register
    def test_register(self):
        response = self.client.post('/api/v1/register', json=users[0])
        self.assertEqual(response.status_code, 201)
        self.assertIn('registration sucessfull', str(response.json))

    # # test with empty data
    # def test_register_without_data(self):
    #     response = self.client.post('/api/v1/register', json=empty)
    #     assert response.status_code == 400
    #     assert 'missing required field' in str(response.json)

    # # test already used email
    # def test_register_existing_email():
    #     response = client.post('/api/v1/register', json=users[0])
    #     assert response.status_code == 409
    #     assert 'user with email already registred' in str(response.json)

    # # test resgister invalid email
    # def test_register_invalid_email():
    #     response = client.post('/api/v1/register', json=users[1])
    #     assert response.status_code == 422
    #     assert 'invalid email' in str(response.json)

    # # test sucess login
    # def test_login():
    #     response = client.post('/api/v1/login', json=users[0])
    #     assert response.status_code == 200
    #     assert 'user logged in' in str(response.json)

    # # test login without data
    # def test_login_without_data():
    #     response = client.post('/api/v1/login', json=empty)
    #     assert response.status_code == 400
    #     assert 'missing required field' in str(response.json)

    # # test login invalid email
    # def test_login_invalid_email():
    #     response = client.post('/api/v1/login', json=users[1])
    #     assert response.status_code == 422
    #     assert 'invalid email' in str(response.json)

    # # test login missing email
    # def test_login_missing_email():
    #     response = client.post('/api/v1/login', json=users[4])
    #     assert response.status_code == 400
    #     assert 'missing required field email' in str(response.json)

    # # test login missing password
    # def test_login_missing_password():
    #     response = client.post('/api/v1/login', json=users[5])
    #     assert response.status_code == 400
    #     assert 'missing required field password' in str(response.json)

    # # test login mismatching password
    # def test_login_invalid_password():
    #     response = client.post('/api/v1/login', json=users[7])
    #     assert response.status_code == 422
    #     assert 'passwords do not match' in str(response.json)

    # # test logout
    # def test_logout():
    #     response = client.post('/api/v1/logout')
    #     assert response.status_code == 200
    #     assert 'logged out' in str(response.json)
