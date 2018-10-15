import pytest
from ... import create_app

from .dummy import users

app = create_app(config_name="testing")
client = app.test_client()


def test_register():
    response = client.post('/api/v1/register', json=users[0])
    assert response.status_code == 200
    assert 'registration sucessfull' in str(response.json)

