import unittest
import json

from .base import BaseTest
from .dummy import products, empty


"""
    Tests for products
"""


class ProductsEndpointsTest(BaseTest):

    # test add products
    def test_add_product(self):
        response = self.client.post('/api/v1/products', 
                                    data=json.dumps(products[0]),
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('shirt', str(response.data))

    # test post same product
    def test_add_same_product(self):
        response = self.client.post('/api/v1/products', 
                                    data=json.dumps(products[0]),
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 409)
        self.assertIn('product with name already exists', str(response.data))

    # test post missing field
    def test_add_missing_field(self):
        response = self.client.post('/api/v1/products', 
                                    data=json.dumps(products[1]),
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 400)
        self.assertIn('missing required field',  str(response.data))

    # test get all products 
    def test_get_all_products(self):
        response = self.client.get('/api/v1/products', 
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)

    # test get sigle item
    def test_get_item_by_id(self):
        response = self.client.get('/api/v1/products/1', 
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)

    # test get item non-existing id 
    def test_get_item_by_non_existing_id(self):
        response = self.client.get('/api/v1/products/20', 
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('product with id 20 does not exist', str(response.data))

    # test get item with str 
    def test_get_item_by_str(self):
        response = self.client.get('/api/v1/products/"20"', 
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 405)
        self.assertIn('int type required', str(response.data))

    # test admin edit product
    def test_edit_product(self):
        response = self.client.post('/api/v1/products/1', 
                                    data=json.dumps(products[3]),
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('vest', str(response.data))

    # test attendant edit product
    def test_attendant_edit_product(self):
        response = self.client.post('/api/v1/products/1',  
                                    data=json.dumps(products[3]),
                                    headers=self.attendant_headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn('unauthorized to perform this function', 
                      str(response.data))

    # test edit nonexisting item 
    def test_edit_non_existing_item(self):
        response = self.client.post('/api/v1/products/20', 
                                    data=json.dumps(products[3]),
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('product with id 20 does not exist', str(response.data))

    # test delete
    def test_delete(self):
        response = self.client.delete('/api/v1/products/1', 
                                      headers=self.admin_headers)
        self.assertEqual(response.status_code, 202)
        self.assertIn('product deleted', str(response.data))

    # test attendant delete
    def test_attendant_delete(self):
        response = self.client.delete('/api/v1/products/1', 
                                      headers=self.attendant_headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn('unauthorized to perform this function', 
                      str(response.data))
