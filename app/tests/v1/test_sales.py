import pytest
from flask import json
from .dummy_data import sales
from .base import BaseTest
from app.api.v1.models.sales import SalesModel

"""
    Tests for sales
"""


class SalesTestEndpoints(BaseTest):

    # test add saless
    def test_add_sales(self):
        response = self.client.post('/api/v1/sales', data=json.dumps(sales[0]),
                                    content_type='application/json',
                                    headers=self.attendant_headers)
        # self.assertEqual(response.status_code, 201)
        self.assertIn('shirt', str(response.data))

    # test post missing field
    def test_add_missing_field(self):
        response = self.client.post('/api/v1/sales', data=json.dumps(sales[1]),
                                    content_type='application/json',
                                    headers=self.attendant_headers)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required parameter', str(response.data))

    # test get all saless
    def test_get_all_sales(self):
        response = self.client.get('/api/v1/sales',
                                   headers=self.admin_headers)
        self.assertEqual(response.status_code, 200)

    # test get sigle item
    def test_get_sale_item_by_id(self):
        response = self.client.get('/api/v1/sales/2',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)

    # test get item non-existing id
    def test_get_sale_item_by_non_existing_id(self):
        response = self.client.get('/api/v1/sales/200',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('sale with id 200 does not exist', str(response.data))

    # test get item with str
    def test_get_item_by_str(self):
        response = self.client.get('/api/v1/sales/"20"',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 404)

    # test admin edit sales
    def test_edit_sales(self):
        response = self.client.put('/api/v1/sales/2',
                                   data=json.dumps(sales[3]),
                                   content_type='application/json',
                                   headers=self.admin_headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('shirt', str(response.data))

    # test attendant edit sales
    def test_attendant_edit_sales(self):
        response = self.client.put('/api/v1/sales/1',
                                   data=json.dumps(sales[3]),
                                   content_type='application/json',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn('unauthorized to perform  function',
                      str(response.data))

    # test edit nonexisting item
    def test_edit_non_existing_item(self):
        response = self.client.put('/api/v1/sales/200',
                                   data=json.dumps(sales[3]),
                                   content_type='application/json',
                                   headers=self.admin_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('Sale with id 200 does not exist', str(response.data))

    # test delete
    def test_delete(self):
        response = self.client.delete('/api/v1/sales/1',
                                      headers=self.admin_headers)
        self.assertEqual(response.status_code, 202)
        self.assertIn('Sale deleted', str(response.data))

    # test attendant delete
    def test_attendant_delete(self):
        response = self.client.delete('/api/v1/sales/1',
                                      headers=self.attendant_headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn('unauthorized to perform  function',
                      str(response.data))

 
 