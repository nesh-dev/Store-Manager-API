import unittest
import json

from .dummy import category, empty
from . base import BaseTest

"""
    Tests for category
"""


class CategoryTestsEndpoints(BaseTest):

    # test add categorys
    def test_add_category(self):
        response = self.client.post('/api/v1/category', 
                                    data=json.dumps(category[0]), 
                                    content_type='application/json',
                                    headers=self.admin_headers)
        # self.assertEqual(response.status_code, 201)
        self.assertIn('clothes', str(response.data))

    # test post same category
    def test_add_same_category(self):
        response = self.client.post('/api/v1/category', 
                                    data=json.dumps(category[0]),
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 409)
        self.assertIn('category with name already exists', 
                      str(response.data))

    # test post missing field
    def test_add_missing_field(self):
        response = self.client.post('/api/v1/category', 
                                    data=json.dumps(category[1]),
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 400)
        self.assertIn('missing required field', str(response.data))

    # test get all categorys 
    def test_get_all_categories(self):
        response = self.client.get('/api/v1/categories', 
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)

    # test get sigle item
    def test_get_item_by_id(self):
        response = self.client.get('/api/v1/category/1', 
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)

    # test get item non-existing id 
    def test_get_item_by_non_existing_id(self):
        response = self.client.get('/api/v1/category/20',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('category with id 20 does not exist', str(response.data))

    # test get item with str 
    def test_get_item_by_str(self):
        response = self.client.get('/api/v1/category/"20"', 
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 405)
        self.assertIn('int type required', str(response.data))

    # test admin edit category
    def test_edit_category(self):
        response = self.client.post('/api/v1/category/1', 
                                    data=json.dumps(category[3]),
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('vest' in str(response.data))

    # test attendant edit category
    def test_attendant_edit_category(self):
        response = self.client.post('/api/v1/category/1', 
                                    data=json.dumps(category[3]),
                                    headers=self.attendant_headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn('unauthorized to perform this function', 
                      str(response.data))

    # test edit nonexisting item 
    def test_edit_non_existing_item(self):
        response = self.client.post('/api/v1/category/20', 
                                    data=json.dumps(category[3]),
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('category with id 20 does not exist', str(response.data))

    # test delete
    def test_delete(self):
        response = self.client.delete('/api/v1/category/1', 
                                      headers=self.admin_headers)
        self.assertEqual(response.status_code, 202)
        self.assertIn('category deleted', str(response.data))

    # test attendant delete
    def test_attendant_delete(self):
        response = self.client.delete('/api/v1/category/1', 
                                      headers=self.attendant_headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn('unauthorized to perform this function', 
                      str(response.data))
