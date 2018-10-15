import pytest
from ... import create_app

from .dummy import users

app = create_app(config_name="testing")
client = app.test_client()


# sucess register
def test_register():
    response = client.post('/api/v1/register', json=users[0])
    assert response.status_code == 200
    assert 'registration sucessfull' in str(response.json)


def test_register_without_data():
    response = client.post('/api/v1/register', json=empty)
    assert response.status_code == 400
    assert 'missing required field' in str(response.json)

