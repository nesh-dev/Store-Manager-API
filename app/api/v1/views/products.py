from flask_restful import reqparse, Resource
import re
# local imports
from ..models.product import ProductModel
from ..middleware.middleware import both_auth


# all categories in list
product_list = ProductModel.get_products()


class ProductListResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("description", type=str, required=True)
    parser.add_argument("category_id", type=int, required=True)
    parser.add_argument("price", type=int, required=True)
    parser.add_argument("quantity", type=int, required=True)
    parser.add_argument("minimum_inventory", type=int, required=True)

    @both_auth
    def get(self):
        """
            Return Product list
        """
        product_list = ProductModel.get_products()
        return product_list

    @both_auth
    def post(self):
        """
            post an item
        """

        data = ProductListResource.parser.parse_args()

        try:
            for k, v in data.items():
                if v == "":
                    return {"message": "{} cannot be an empty".format(k)}
        except:
            pass

        Product_id = len(product_list) + 1
        if ProductModel.get_by_name(data['name'], product_list):
            return {"message": "Product with name already exist"}, 409

        Product_input = {
                         "id": Product_id, "name": data["name"],
                         "description": data["description"],
                         "category_id": data["category_id"],
                         "price": data["price"],
                         "quantity": data["quantity"],
                         "minimum_inventory": data["minimum_inventory"]
                        }

        ProductModel.add_product(Product_input)
        Product = ProductModel.get_by_id(Product_id, product_list)
        return Product, 201


class ProductResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("description", type=str, required=True)
    parser.add_argument("category_id", type=int, required=True)
    parser.add_argument("price", type=int, required=True)
    parser.add_argument("quantity", type=int, required=True)
    parser.add_argument("minimum_inventory", type=int, required=True)

    @both_auth
    def get(self, id):
        """
            get by id
        """
        message = "Product with id {} does not exist".format(id)
        Product = ProductModel.get_by_id(id, product_list)
        if Product:
            return Product, 200
        return {"message": message}, 404

    @both_auth
    def put(self, id):
        """
            edit the Product
        """

        # validate empty string inputs 
        try:
            for k, v in data.items():
                if v == "":
                    return {"message": "{} cannot be an empty".format(k)}
        except:
            pass

        message = "Product with id {} does not exist".format(id)
        data = ProductResource.parser.parse_args()
        item_to_edit = ProductModel.get_by_id(id, product_list)
        if item_to_edit:
            item_to_edit.update(data)
            return item_to_edit, 201
        return {"message": message}, 404

    @both_auth
    def delete(self, id):
        message = "Product with id {} does not exist".format(id)
        length = ProductModel.get_length(product_list) 
        item_to_delete = ProductModel.get_by_id(id, product_list)
        if item_to_delete:
            ProductModel.delete(id, product_list)
            return {"message": "Product deleted"}, 202
        return {"message": message}
        