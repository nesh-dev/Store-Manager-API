# import unittest

# from .base import BaseTest
# from .dummy import products, empty


# """
#     Tests for products
# """


# class ProductsEndpointsTest(BaseTest):

#     # test add products
#     def test_add_product(self):
#         response = self.client.post('/api/v1/products', json=products[0],
#                                     headers=self.admin_headers)
#         self.assertEqual(response.status_code, 201)
#         self.assertIn('shirt', str(response.json)


#     # test post same product
#     def test_add_same_product(self):
#         response = self.client.post('/api/v1/products', json=products[0],
#                             headers=self.admin_headers)
#         self.assert( response.status_code == 409
#         self.assert( 'product with name already exists' in str(response.json)

#     # test post missing field
#     def test_add_missing_field(self):
#         response = self.client.post('/api/v1/products', json=products[1],
#                             headers=self.admin_headers)
#         self.assert( response.status_code == 400
#         self.assert( 'missing required field' in str(response.json)

#     # test get all products 
#     def test_get_all_products(self):
#         response = self.client.get('/api/v1/products', headers=self.attendant_headers)
#         self.assert( response.status_code == 200


#     # test get sigle item
#     def test_get_item_by_id(self):
#         response = self.client.get('/api/v1/products/1', headers=self.attendant_headers)
#         self.assert( response.status_code == 200

#     # test get item non-existing id 
#     def test_get_item_by_non_existing_id(self):
#         response = self.client.get('/api/v1/products/20', headers=self.attendant_headers)
#         self.assert( response.status_code == 404
#         self.assert( 'product with id 20 does not exist' in str(response.json)

#     # test get item with str 
#     def test_get_item_by_str(self):
#         response = self.client.get('/api/v1/products/"20"', headers=self.attendant_headers)
#         self.assert( response.status_code == 405
#         self.assert( 'int type required' in str(response.json)

#     # test admin edit product
#     def test_edit_product(self):
#         response = self.client.post('/api/v1/products/1', json=products[3],
#                             headers=self.self.admin_headers)
#         self.assert( response.status_code == 201
#         self.assert( 'vest' in str(response.json)

#     # test attendant edit product
#     def test_attendant_edit_product(self):
#         response = self.client.post('/api/v1/products/1', json=products[3],
#                             headers=attendnt_headers)
#         self.assert( response.status_code == 401
#         self.assert( 'unauthorized to perform this function' in str(response.json)

#     # test edit nonexisting item 
#     def test_edit_non_existing_item(self):
#         response = self.client.post('/api/v1/products/20', json=products[3],
#                             headers=self.self.admin_headers)
#         self.assert( response.status_code == 404
#         self.assert( 'product with id 20 does not exist' in str(response.json)

#     # test delete
#     def test_delete(self):
#         response = self.client.delete('/api/v1/products/1', headers=self.self.admin_headers)
#         self.assert( response.status_code == 202
#         self.assert( 'product deleted' in str(response.json)

#     # test attendant delete
#     def test_attendant_delete(self):
#         response = self.self.client.delete('/api/v1/products/1', headers=self.attendant_headers)
#         self.assert( response.status_code == 401
#         self.assert( 'unauthorized to perform this function' in str(response.json)
