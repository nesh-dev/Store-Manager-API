""" use unittesting module as testing framework"""
import unittest
import json
from app.api.v1.models.auth import userModel
from app.api.v1.models.category import categoryModel
from app.api.v1.models.product import productModel
from app.api.v1.models.sales import salesModel
from .dummy_data import users, category, products, sales

from ... import create_app


class BaseTest(unittest.TestCase):
    """
        Base Class for all tests to inherit
    """

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
        categoryModel.add_category(category[0])

        # create a test prodct
        productModel.add_product(products[0])

        # create a test sale
        salesModel.add_sales(sales[0])

    def tearDown(self):
        with self.app.app_context():
            categoryModel.drop()
            productModel.drop()
            salesModel.drop()
            userModel.drop()
