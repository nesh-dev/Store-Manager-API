import pytest
from ... import create_app

from .dummy import users, empty


"""
    Tests for user auth
"""


# app instance as test
app = create_app(config_name="testing")
client = app.test_client()


# sucess register
def test_register():
    response = client.post('/api/v1/register', json=users[0])
    assert response.status_code == 200
    assert 'registration sucessfull' in str(response.json)


# test with empty data
def test_register_without_data():
    response = client.post('/api/v1/register', json=empty)
    assert response.status_code == 400
    assert 'missing required field' in str(response.json)


# test already used email
def test_register_existing_email():
    response = client.post('/api/v1/register', json=users[0])
    assert response.status_code == 409
    assert 'user with email already registred' in str(response.json)


# test resgister invalid email
def test_register_invalid_email():
    response = client.post('/api/v1/register', json=users[1])
    assert response.status_code == 422
    assert 'invalid email' in str(response.json)


# test sucess login 
def test_login():
    response = client.post('/api/v1/login', json=users[0])
    assert response.status_code == 200 
    assert 'user logged in' in str(response.json)


# test login without data 
def test_login_without_data():
    response = client.post('/api/v1/login', json=empty)
    assert response.status_code == 400
    assert 'missing required field' in str(response.json)


# test login invalid email
def test_login_invalid_email():
    response = client.post('/api/v1/login', json=users[1])
    assert response.status_code == 422
    assert 'invalid email' in str(response.json)

