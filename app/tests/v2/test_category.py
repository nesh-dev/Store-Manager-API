
import json
from .dummy_data import category, category_product
from . base import BaseTest


class CategoryTestsEndpoints(BaseTest):

    """
        Tests for category
    """

    def test_add_category(self):
        """
            test add categorys
        """
        response = self.client.post('/api/v2/categories',
                                    data=json.dumps(category[4]),
                                    content_type='application/json',
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('electronics', str(response.data))

    def test_add_same_category(self):
        """
            test post same category
        """
        response = self.client.post('/api/v2/categories',
                                    data=json.dumps(category[0]),
                                    content_type='application/json',
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 409)
        self.assertIn('category with name already exist',
                      str(response.data))

    def test_add_missing_field(self):
        """test post missing field"""
        response = self.client.post('/api/v2/categories',
                                    data=json.dumps(category[1]),
                                    content_type='application/json',
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required parameter', str(response.data))

    def test_get_all_categories(self):
        """test get all categorys"""
        response = self.client.get('/api/v2/categories',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)

    def test_get_item_by_id(self):
        """test get all categorys"""
        response = self.client.get('/api/v2/category/1',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)

    def test_get_non_existent_item(self):
        """test get all categories"""

        response = self.client.get('/api/v2/category/200',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('item category_id does not exist',
                      str(response.data))

    def test_get_item_by_str(self):
        """test get item with str"""
        response = self.client.get('/api/v2/category/"20"',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 404)

    def test_edit_category(self):
        """test admin edit category"""
        response = self.client.put('/api/v2/category/1',
                                   data=json.dumps(category[3]),
                                   content_type='application/json',
                                   headers=self.admin_headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Apparels', str(response.data))

    def test_edit_non_existing_item(self):
        """test edit nonexisting item"""
        response = self.client.put('/api/v2/category/200',
                                   data=json.dumps(category[3]),
                                   content_type='application/json',
                                   headers=self.admin_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('"category with id 200 does not exist',
                      str(response.data))

    def test_categories_product(self):
        """test add prodcts to categories"""
        response = self.client.post('api/v2/cat/products',
                                    data=json.dumps(category_product[0]),
                                    content_type='application/json',
                                    headers=self.attendant_headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('shirt', str(response.data))

    def test_categories_product_admin(self):
        """test add prodcts to categories"""
        response = self.client.post('api/v2/cat/products',
                                    data=json.dumps(category_product[0]),
                                    content_type='application/json',
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn('unauthorized', str(response.data))

    def test_categories_in_porducts(self):
        """test products in the categories"""
        response = self.client.post('api/v2/cat/products',
                                    data=json.dumps(category_product[0]),
                                    content_type='application/json',
                                    headers=self.attendant_headers)
        response = self.client.get('api/v2/cat/products',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)
    

    def test_delete(self):
        """test delete"""
        response = self.client.delete('/api/v2/category/1',
                                      headers=self.admin_headers)
        self.assertEqual(response.status_code, 202)
        self.assertIn('Category deleted', str(response.data))
