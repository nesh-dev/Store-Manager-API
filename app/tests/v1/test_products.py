import pytest
from ... import create_app

from .dummy import products, empty
from .headers import attendant_headers, admin_headers


"""
    Tests for products
"""


# app instance as test
app = create_app(config_name="testing")
client = app.test_client()



