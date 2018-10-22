
import json
from .dummy_data import sales
from .base import BaseTest


class SalesTestEndpoints(BaseTest):

    """
    Tests for sales
    """

    def test_add_sales(self):
        """
          test add saless
        """
        response = self.client.post('/api/v1/sales', data=json.dumps(sales[0]),
                                    content_type='application/json',
                                    headers=self.attendant_headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('vest', str(response.data))

    def test_add_missing_field(self):
        """ test post missing field """
        response = self.client.post('/api/v1/sales', data=json.dumps(sales[1]),
                                    content_type='application/json',
                                    headers=self.attendant_headers)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required parameter', str(response.data))

    def test_get_all_sales(self):
        """
          test get all sales
        """
      
        response = self.client.get('/api/v1/sales',
                                   headers=self.admin_headers)
        self.assertEqual(response.status_code, 200)

    def test_get_sale_item_by_id(self):
        """ test get sigle item """
        response = self.client.get('/api/v1/sales/1',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 200)

    def test_sale_nonexistent(self):
        """test get item non-existing id"""
        response = self.client.get('/api/v1/sales/200',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('sale with id 200 does not exist', str(response.data))

    
    def test_get_item_by_str(self):
        """test get item with str"""
        response = self.client.get('/api/v1/sales/"20"',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 404)

    def test_edit_sales(self):
        """test admin edit sales"""
        response = self.client.put('/api/v1/sales/1',
                                   data=json.dumps(sales[3]),
                                   content_type='application/json',
                                   headers=self.admin_headers)
        self.assertEqual(response.status_code, 201)
        # self.assertIn('shirt', str(response.data))

    def test_attendant_edit_sales(self):
        """test attendant edit sales"""
        response = self.client.put('/api/v1/sales/1',
                                   data=json.dumps(sales[3]),
                                   content_type='application/json',
                                   headers=self.attendant_headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn('unauthorized to perform  function',
                      str(response.data))

    def test_edit_non_existing_item(self):
        """# test edit nonexisting item"""
        response = self.client.put('/api/v1/sales/200',
                                   data=json.dumps(sales[3]),
                                   content_type='application/json',
                                   headers=self.admin_headers)
        self.assertEqual(response.status_code, 404)
        self.assertIn('Sale with id 200 does not exist', str(response.data))

    def test_attendant_delete(self):
        """test attendant delete"""
        response = self.client.delete('/api/v1/sales/1',
                                      headers=self.attendant_headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn('unauthorized to perform  function',
                      str(response.data))
