from flask_restful import reqparse, Resource
from flask_jwt_extended import get_jwt_identity
from ..models.sales import SalesModel 
from ..models.auth import UserModel
from ...middleware.middleware import (admin_allowed, both_roles_allowed,
                                      attendant_allowed)


class SalesListResource(Resource):
    """ sales list resource"""
    parser = reqparse.RequestParser()
    parser.add_argument("sale_items", type=dict, action='append', 
                        required=True)
    parser.add_argument("customer", type=str, required=True)
  
    @attendant_allowed
    def post(self): 
        """ save products """
        data = SalesListResource.parser.parse_args()
        current_user = get_jwt_identity()
        user_id = current_user[0]
        user = UserModel()
        user = user.get_item('users', user_id=user_id)
        attendant_email = user['email']
        attendant = attendant_email
        name = data['customer']

        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}
    
        sale_list = data['sale_items']

        # validate items in sale_list
        for item in sale_list:
            if item.get('product_id') is None:
                return {"message": "missing required field product_id"}, 400
            elif item.get('quantity') is None:
                return {"message": "missing required field quantity"}, 400
            elif type(item['product_id']) != int:
                return {"message": "product_id should be of type int"}, 400
            elif type(item['quantity']) != int:
                return {"message": "quantity should be of type int"}, 400
        sale = SalesModel(customer=name)
        complete_sale = sale.create_sale(attendant, sale_list)
        return complete_sale

    @admin_allowed
    def get(self):

        sale = SalesModel()
        all_sales = sale.get_all('sales')
        return all_sales


class SalesResource(Resource):
    """ has get and delete endpoints for the sales """
    @admin_allowed
    def get(self, id):
        """ get a particular sale via its id """

        sale = SalesModel()
        sale_to_get = sale.get_item('sales', sale_id=id)
        message = "sale with id {} does not exist".format(id)
        if sale_to_get:
            return sale_to_get
        return {"message": message}, 404

    @admin_allowed
    def delete(self, id):
        sale = SalesModel()
        sale_to_delete = sale.get_item('sales', sale_id=id)
        message = "Sale with id {} does not exist".format(id)
        if sale_to_delete:
            sale.delete('sales', sale_id=id)
            return {"message": "Sale deleted"}, 202
        return {"message": message}


class AttendatSales(Resource):
    """ get sales of a specific user """
    @admin_allowed
    def get(self, email):
        """ get a user sales based on their email """
        sale = SalesModel()
        users_sales = sale.get_all_with('sales', attendant_email=email)
        return users_sales

        
