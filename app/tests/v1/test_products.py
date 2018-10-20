
import json
from .base import BaseTest
from .dummy_data import products


class ProductsEndpointsTest(BaseTest):
    """
        Test products resource
    """

    
    def test_add_product(self):

        """
            test add products
        """
        response = self.client.post('/api/v1/products',
                                    data=json.dumps(products[4]),
                                    content_type='application/json',
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('trouser', str(response.data))

    
    def test_add_same_product(self):
        """"test post same product"""
        response = self.client.post('/api/v1/products',
                                    data=json.dumps(products[0]),
                                    content_type='application/json',
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 409)
        self.assertIn('Product with name already exist', str(response.data))

   
    def test_product_add_missing_field(self):
        """ test post missing field"""
        response = self.client.post('/api/v1/products',
                                    data=json.dumps(products[1]),
                                    content_type='application/json',
                                    headers=self.admin_headers)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required parameter', str(response.data))

    def test_get_all_products(self):
        """ test get all products"""
        response = self.client.get('/api/v1/products',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)

    def test_get_product_item_by_id(self):
        """ test get sigle item """
        response = self.client.get('/api/v1/products/1',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)
    
    def test_product_get_nonexistent(self):
        """" test get item non-existing id """
        response = self.client.get('/api/v1/products/200',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('Product with id 200 does not exist', str(response.data))

    def test_product_get_item_by_str(self):
        """test get item with str"""
        response = self.client.get('/api/v1/products/"20"',
                                   content_type='application/json',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 404)

    def test_edit_product(self):
        """test admin edit product"""
        response = self.client.put('/api/v1/products/1',
                                   data=json.dumps(products[3]),
                                   content_type='application/json',
                                   headers=self.admin_headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('vest', str(response.data))

    def test_edit_non_existing_item(self):
        """
            # test edit nonexisting item
        """
        response = self.client.put('/api/v1/products/200',
                                   data=json.dumps(products[3]),
                                   content_type='application/json',
                                   headers=self.admin_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('Product with id 200 does not exist', str(response.data))

    def test_delete_prouct(self):
        """
            test delete
        """
        response = self.client.delete('/api/v1/products/1',
                                      headers=self.admin_headers)
        self.assertEqual(response.status_code, 202)
        self.assertIn('Product deleted', str(response.data))
