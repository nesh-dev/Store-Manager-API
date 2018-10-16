import pytest
from ... import create_app

from .dummy import products, empty

# get auth headers for protected endpoints
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
    assert 'shirt' in str(response.json)


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


# test get all products 
def test_get_all_products():
    response = client.get('/api/v1/products', headers=attendant_headers)
    assert response.status_code == 200


# test get sigle item
def test_get_item_by_id():
    response = client.get('/api/v1/products/1', headers=attendant_headers)
    assert response.status_code == 200


# test get item non-existing id 
def test_get_item_by_non_existing_id():
    response = client.get('/api/v1/products/20', headers=attendant_headers)
    assert response.status_code == 404
    assert 'product with id 20 does not exist' in str(response.json)


# test get item with str 
def test_get_item_by_str():
    response = client.get('/api/v1/products/"20"', headers=attendant_headers)
    assert response.status_code == 405
    assert 'int type required' in str(response.json)


# test admin edit product
def test_edit_product():
    response = client.post('/api/v1/products/1', json=products[3],
                           headers=admin_headers)
    assert response.status_code == 201
    assert 'vest' in str(response.json)



