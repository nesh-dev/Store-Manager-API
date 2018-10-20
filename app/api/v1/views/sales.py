import re
from flask_restful import reqparse, Resource
from flask_jwt_extended import get_jwt_identity

# local imports
from ..models.sales import salesModel
from ..models.product import productModel
from ..middleware.middleware import (both_roles_allowed,
                                     admin_allowed,
                                     attendant_allowed)
# get all sales in list
sales_list = salesModel.get_sales()


class SalesListResource(Resource):
    """
        handles the get all and post
    """

    parser = reqparse.RequestParser()
    parser.add_argument("product_id", type=int, required=True)
    parser.add_argument("quantity", type=int, required=True)
    parser.add_argument("customer", type=str, required=True)

    @admin_allowed
    def get(self):
        """
            Get a list of all the sales 
        """
        if not sales_list:
            return {"message": "no sale saved"}, 404
        return sales_list

    @attendant_allowed
    def post(self):
        """
            Post a new sale item
            by getting the products id, 
            get the identity of the sale attendant working on it 
            calculating the total sale from the products price and quantity

        """
        data = SalesListResource.parser.parse_args()

        # validate all inputs not to be empty
        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

        # get the attendant details

        current_user = get_jwt_identity()
        user = current_user["email"]

        # increment sale by id
        sales_id = len(sales_list) + 1

        # custom message for missing product
        message = "no product with id {}".format(data["product_id"])

        # get the category name by id
        product = productModel.get_by_id(data["product_id"],
                                         productModel.get_products())

        if product:
            # get category name via its key  name
            product_name = product['name']

            # calculate the price
            price = product["price"]
            total = salesModel.calculate_total(price, data['quantity'])

            # prodct item to be saved
            sale_input = {
                "id": sales_id, "product": product_name,
                "quantity": data['quantity'],
                "attendant": user,
                "total": total}

            salesModel.add_sales(sale_input)
            sale = salesModel.get_by_id(sales_id, sales_list)
            return sale, 201
        return {"message": message}, 404


class SaleResource(Resource):

    """
        Handles get specific , modify and delete
    """
    parser = reqparse.RequestParser()
    parser.add_argument("product_id", type=int, required=True)
    parser.add_argument("quantity", type=int, required=True)
    parser.add_argument("customer", type=str, required=True)

    @both_roles_allowed
    def get(self, id):

        # get the user passing the request
        current_user = get_jwt_identity()
        # get unique identity via email
        user = current_user["email"]

        # gget the users role
        role = current_user["role"]

        # get the sale via its id
        sale = salesModel.get_by_id(id, sales_list)

        if sale:

            # get the attendants email who worked on the sale
            attendant = sale["attendant"]

            # check if the user owns the sale or is admin via role
            if (user == attendant) or (role == 2):
                return sale, 200
            # if not they are not authorized
            return {"message": "no authorization to view sale"}, 401
        #
        return {"message": "sale with id {} does not exist".format(id)}, 404

    @admin_allowed
    def put(self, id):

        # get all inputs
        data = SaleResource.parser.parse_args()

        # validate empty string inputs
        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

        # error message to return
        message = "Sale with id {} does not exist".format(id)

        # get the item to edit
        item_to_edit = salesModel.get_by_id(id, sales_list)
        if item_to_edit:
            # update the item
            item_to_edit.update(data)
            return item_to_edit, 201
        return {"message": message}, 404

    @admin_allowed
    def delete(self, id):

        # error message to be returned
        message = "Sale with id {} does not exist".format(id)

        # get the item to delete
        item_to_delete = salesModel.get_by_id(id, sales_list)
        if item_to_delete:

            # delete the sale
            salesModel.delete(id, sales_list)

            # return message
            return {"message": "Sale deleted"}, 202
        return {"message": message}
