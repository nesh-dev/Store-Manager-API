import unittest 
import json
from ... import create_app

from .dummy_data import users, empty, category, products, sales
from app.api.v1.models.auth import UserModel
from app.api.v1.models.category import CategoryModel
from app.api.v1.models.product import ProductModel
from app.api.v1.models.sales import SalesModel


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()

        # to handle error in tests
        self.client.post('api/v1/register', data=json.dumps(users[0]),
                         content_type='application/json')
        user = self.client.post('api/v1/login', data=json.dumps(users[0]),
                                content_type='application/json')
        attendant_token = user.get_json().get('access_token')

        # handle error in tests
        self.client.post('api/v1/register', data=json.dumps(users[9]),
                         content_type='application/json')
        user = self.client.post('api/v1/login', data=json.dumps(users[9]),
                                content_type='application/json')
        admin_token = user.get_json().get('access_token')

        self.admin_headers = {
            'Authorization': 'Bearer {}'.format(admin_token),
            'Content-Type': 'application/json'}

        self.attendant_headers = {
            'Authorization': 'Bearer {}'.format(attendant_token),
            'Content-Type': 'application/json'
            }

        # create a test category 
        self.client.post('/api/v1/categories',
                         data=json.dumps(category[0]),
                         content_type='application/json',
                         headers=self.admin_headers)

        # create a test prodct
        self.client.post('/api/v1/products',
                         data=json.dumps(products[0]),
                         content_type='application/json',
                         headers=self.attendant_headers)
        # create a test sale
        self.client.post('/api/v1/sales',
                         data=json.dumps(sales[0]),
                         content_type='application/json',
                         headers=self.attendant_headers)

        def tearDown(self):

            UserModel.drop(UserModel.get_users())
            CategoryModel.drop(CategoryModel.get_categories())
            ProductModel.drop(ProductModel.get_products())
            SalesModel.drop(SalesModel.get_sales())
