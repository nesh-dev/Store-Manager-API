from flask_restful import reqparse, Resource

from ...middleware.middleware import admin_allowed, both_roles_allowed
from ..models.products import ProductsModel 


class ProductListResource(Resource):
    """ products list resource"""
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("description", type=str, required=True)
    parser.add_argument("price", type=int, required=True)
    parser.add_argument("quantity", type=int, required=True)
 
    @admin_allowed
    def post(self): 
        """ save products """
        data = ProductListResource.parser.parse_args()

        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}
    
        name = data['name']
        description = data['description']
        price = data['price']
        quantity = data['quantity']
        product = ProductsModel(name=name, description=description, 
                                price=price, quantity=quantity)
        product_with_name = product.get_item('products', name=name)

        # if item exists a tuple with message and error is returned
        if type(product_with_name) is tuple:
            return product.create_product(), 201
        return {"message": "Product with name already exist"}, 409

    @both_roles_allowed
    def get(self):
        product = ProductsModel()
        return product.get_all('products')


class ProductsResource(Resource):
    """ has endpoints for edit, get and delete"""
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("description", type=str, required=True)
    parser.add_argument("price", type=int, required=True)
    parser.add_argument("quantity", type=int, required=True)
    parser.add_argument("minimum_inventory", type=int, required=True)

    @both_roles_allowed
    def get(self, id):
        """get a product by id """
        product = ProductsModel()
        product_to_get = product.get_item('products', product_id=id)
        message = "Product with id {} does not exist".format(id)
        if product_to_get:
            return product_to_get
        return {"message": message}, 404

    @admin_allowed
    def put(self, id):
        
        """update a product """
        data = ProductsResource.parser.parse_args()
        # validate inputs
        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

        name = data['name']
        description = data['description']
        price = data['price']
        quantity = data['quantity']
        minimum_inventory = data['minimum_inventory']
        message = "Product with id {} does not exist".format(id)
        product = ProductsModel()
        product_to_update = product.get_item('products', product_id=id)
        # import pdb; pdb.set_trace()
        if type(product_to_update) is not tuple:
            return product.update_products(id, name=name,
                                           description=description,
                                           quantity=quantity, 
                                           price=price, 
                                           minimum_inventory=minimum_inventory
                                           ), 201
        return {"message": message}, 404

    @admin_allowed
    def delete(self, id):
        product = ProductsModel()
        product_to_delete = product.get_item('products', product_id=id)
        message = "Product with id {} does not exist".format(id)
        if product_to_delete:
            product.delete('products', product_id=id)
            return {"message": "Product deleted"}, 202
        return {"message": message}


class SearchProduct(Resource):

    def get(self, name):
        product = ProductsModel()
        product_to_get = product.get_item('products', name=name)
        message = "Product with id {} does not exist".format(id)
        if product_to_get:
            return product_to_get
        return {"message": message}, 404
