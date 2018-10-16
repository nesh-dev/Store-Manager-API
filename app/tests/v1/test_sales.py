import pytest
from flask import json
from .dummy import sales, empty
from .base import BaseTest

"""
    Tests for sales
"""


class SalesTestEndpoints(BaseTest):

    # test add saless
    def test_add_sales(self):
        response = self.client.post('/api/v1/sales', data=json.dumps(sales[0]),
                                    headers=self.admin_headers)
        # self.assertEqual(response.status_code, 201)
        res = json.loads(response.data)
        self.assertIn('clothes', response['message'])

    # # test post same sales
    # def test_add_same_sales(self):
    #     response = self.client.post('/api/v1/sales', data=json.dumps(sales[0]),
    #                                 headers=self.admin_headers)
    #     self.assertEqual(response.status_code, 409)
    #     self.assertIn('sales with name already exists',
    #                   str(response.))

    # # test post missing field
    # def test_add_missing_field(self):
    #     response = self.client.post('/api/v1/sales', json=sales[1],
    #                                 headers=self.admin_headers)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertIn('missing required field', str(response.json))

    # # test get all saless 
    # def test_get_all_categories(self):
    #     response = self.client.get('/api/v1/sales', 
    #                                headers=self.attendant_headers)
    #     self.assertEqual(response.status_code, 200)

    # # test get sigle item
    # def test_get_item_by_id(self):
    #     response = self.client.get('/api/v1/sales/1',
    #                                headers=self.attendant_headers)
    #     self.assertEqual(response.status_code, 200)

    # # test get item non-existing id 
    # def test_get_item_by_non_existing_id(self):
    #     response = self.client.get('/api/v1/sales/20', 
    #                                headers=self.attendant_headers)
    #     self.assertEqual(response.status_code, 404)
    #     self.assertIn('sales with id 20 does not exist', str(response.json))

    # # test get item with str 
    # def test_get_item_by_str(self):
    #     response = self.client.get('/api/v1/sales/"20"', 
    #                                headers=self.attendant_headers)
    #     self.assertEqual(response.status_code, 405)
    #     self.assertIn('int type required', str(response.json))

    # # test admin edit sales
    # def test_edit_sales(self):
    #     response = self.client.post('/api/v1/sales/1', json=sales[3],
    #                                 headers=self.admin_headers)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn('vest', str(response.json))

    # # test attendant edit sales
    # def test_attendant_edit_sales(self):
    #     response = self.client.post('/api/v1/sales/1', json=sales[3],
    #                                 headers=self.attendant_headers)
    #     self.assertEqual(response.status_code, 401)
    #     self.assertIn('unauthorized to perform this function',
    #                   str(response.json))

    # # test edit nonexisting item 
    # def test_edit_non_existing_item(self):
    #     response = self.client.post('/api/v1/sales/20', json=sales[3],
    #                                 headers=self.admin_headers)
    #     self.assertEqual(response.status_code, 404)
    #     self.assertIn('sales with id 20 does not exist', str(response.json))

    # # test delete
    # def test_delete(self):
    #     response = self.client.delete('/api/v1/sales/1', 
    #                                   headers=self.admin_headers)
    #     self.assertEqual(response.status_code, 202)
    #     self.assertIn('sales deleted', str(response.json))

    # # test attendant delete
    # def test_attendant_delete(self):
    #     response = self.client.delete('/api/v1/sales/1',
    #                                   headers=self.attendant_headers)
    #     self.assertEqual(response.status_code, 401)
    #     self.assertIn('unauthorized to perform this function', 
    #                   str(response.json))
