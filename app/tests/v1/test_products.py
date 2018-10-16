import pytest
from ... import create_app

from .dummy import products, empty

# get auth headers for protected endpoint
from .headers import attendant_headers, admin_headers


"""
    Tests for products
"""


# app instance as test
app = create_app(config_name="testing")
client = app.test_client()


# test add products
def test_add_product():
    response = client.post('/api/v1/products', json=products[0],
                           headers=attendant_headers)
    assert response.status_code == 201
    assert 'product created' in str(response.json)
