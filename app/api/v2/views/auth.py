import datetime
import re 
from flask_restful import reqparse, Resource
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_raw_jwt)

# local imports 
from ..models.auth import UserModel
from ...middleware.middleware import both_roles_allowed


class SignupResource(Resource):
    """
        Register user endpint
    """
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('confirm_password', type=str, required=True)
    parser.add_argument('email', type=str, required=True)

    def post(self):
        data = SignupResource().parser.parse_args()

        # validations for input
        # eliminate space in username
        username = ''.join(data['username'].split())

        if not re.match(
                        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                data['email']):
            return {"message": "invalid email"}, 422
        elif len(data['password']) < 6:
            return {"message":
                    "password should atleast six characters long"}

        elif data['username'] == "":
            return {"message": "username should not be empty"}
        elif data['confirm_password'] != data["password"]:
            return {"message": "passwords do not match"}

        user = UserModel(username=username, 
                         email=data['email'], 
                         password=data['password'])

        user_with_email = user.get_item('users', email=data['email'])
        if user_with_email:
            return {"message": "user with email already registred"}, 409
    
        user.create_user()
        return {"message": "registration sucessfull"}, 201




