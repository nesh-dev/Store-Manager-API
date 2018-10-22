import re
from flask_restful import reqparse, Resource

# local imports
from ..models.product import productModel
from ..models.category import categoryModel
from ..middleware.middleware import admin_allowed, both_roles_allowed


# all categories in list
product_list = productModel.get_products()


class ProductListResource(Resource):

    " cotain the GET and POST requests for products "
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("description", type=str, required=True)
    parser.add_argument("price", type=int, required=True)
    parser.add_argument("quantity", type=int, required=True)
    parser.add_argument("minimum_inventory", type=int, required=True)

    @both_roles_allowed
    def get(self):
        """
            Return items stored in products
        """
        if not product_list:
            return {"message": "no product saved"}, 404
        return product_list

    @admin_allowed
    def post(self):
        """
            post an item
        """

        data = ProductListResource.parser.parse_args()

        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

        Product_id = len(product_list) + 1
        if productModel.get_by_name(data['name'], product_list):
            return {"message": "Product with name already exist"}, 409

        # custom message for missing category
        # prodct item to be saved
        Product_input = {
            "id": Product_id, "name": data["name"],
            "description": data["description"],
            "price": data["price"],
            "quantity": data["quantity"],
            "minimum_inventory": data["minimum_inventory"]
        }
        productModel.add_product(Product_input)
        Product = productModel.get_by_id(Product_id, product_list)
        return Product, 201


class ProductResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("description", type=str, required=True)
    parser.add_argument("category_id", type=int, required=True)
    parser.add_argument("price", type=int, required=True)
    parser.add_argument("quantity", type=int, required=True)
    parser.add_argument("minimum_inventory", type=int, required=True)

    @both_roles_allowed
    def get(self, id):
        """
            get by id
        """
        message = "Product with id {} does not exist".format(id)
        Product = productModel.get_by_id(id, product_list)
        if Product:
            return Product, 200
        return {"message": message}, 404

    @admin_allowed
    def put(self, id):
        """
            edit the Product get by id 
            and manipulate data
        """
        data = ProductResource.parser.parse_args()
    # validate empty string inputs
        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

        message = "Product with id {} does not exist".format(id)

        item_to_edit = productModel.get_by_id(id, product_list)
        if item_to_edit:
            item_to_edit.update(data)
            return item_to_edit, 201
        return {"message": message}, 404

    @admin_allowed
    def delete(self, id):
        message = "Product with id {} does not exist".format(id)
        item_to_delete = productModel.get_by_id(id, product_list)
        if item_to_delete:
            productModel.delete(id, product_list)
            return {"message": "Product deleted"}, 202
        return {"message": message}, 404
