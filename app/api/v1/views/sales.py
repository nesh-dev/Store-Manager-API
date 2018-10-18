from flask_restful import reqparse, Resource
from flask_jwt_extended import get_jwt_identity

import re
# local imports
from ..models.sales import SalesModel
from ..models.product import ProductModel
from ..middleware.middleware import both_auth, admin_auth, attendant_auth

sales_list = SalesModel.get_sales()


class SalesListResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("product_id", type=int, required=True)
    parser.add_argument("quantity", type=int, required=True)
    parser.add_argument("customer", type=str, required=True)

    @admin_auth
    def get(self):
        return sales_list

    @attendant_auth
    def post(self):

        data = SalesListResource.parser.parse_args()

        try:
            for k, v in data.items():
                if v == "":
                    return {"message": "{} cannot be an empty".format(k)}
        except:
            pass

        # get the attendant details 

        current_user = get_jwt_identity()
        username = current_user["username"]

        # increment sale by id
        sales_id = len(sales_list) + 1

        # custom message for missing product
        message = "no product with id {}".format(data["product_id"])

        # get the category name by id
        product = ProductModel.get_by_id(data["product_id"], 
                                         ProductModel.get_products())

        if product:
            # get category name via its key  name 
            product_name = product['name']

            # calculate the price
            price = product["price"]
            total = SalesModel.calculate_total(price, data['quantity'])

            # prodct item to be saved
            sale_input = {
                                "id": sales_id, "product": product_name,
                                "quantity": 3, "attendant": username, 
                                "total": total
                            }
            SalesModel.add_sales(sale_input)
            sale = SalesModel.get_by_id(sales_id, sales_list)
            return sale, 201
        return {"message": message}, 404


class SaleResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("product_id", type=int, required=True)
    parser.add_argument("quantity", type=int, required=True)
    parser.add_argument("customer", type=str, required=True)

    @both_auth
    def get(self, id):
        current_user = get_jwt_identity()
        username = current_user["username"]
        role = current_user["role"]

        sale = SalesModel.get_by_id(id, sales_list) 

        if sale:
            attendant = sale["attendant"] 
            if (username == attendant) or (role == 2):
                return sale, 200
            return {"message": "not authorization to view sale"}, 401
        return {"message": "sale with id {} does not exist".format(id)}, 404

    @admin_auth
    def put(self, id):
        
        data = SaleResource.parser.parse_args()
        # validate empty string inputs 
        try:
            for k, v in data.items():
                if v == "":
                    return {"message": "{} cannot be an empty".format(k)}
        except:
            pass

        message = "Sale with id {} does not exist".format(id)
        item_to_edit = SalesModel.get_by_id(id, sales_list)
        if item_to_edit:
            item_to_edit.update(data)
            return item_to_edit, 201
        return {"message": message}, 404

    @admin_auth
    def delete(self, id):
        message = "Sale with id {} does not exist".format(id)
        item_to_delete = SalesModel.get_by_id(id, sales_list)
        if item_to_delete:
            SalesModel.delete(id, sales_list)
            return {"message": "Sale deleted"}, 202
        return {"message": message}