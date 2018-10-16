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

# test post same product
    def test_add_same_product():
        response = client.post('/api/v1/products', json=products[0],
                               headers=attendant_headers)
        assert response.status_code == 409
        assert 'product with name already exists' in str(response.json)

# test post missing field
    def test_add_missing_field():
        response = client.post('/api/v1/products', json=products[1],
                               headers=attendant_headers)
        assert response.status_code == 400
        assert 'missing required field' in str(response.json)


