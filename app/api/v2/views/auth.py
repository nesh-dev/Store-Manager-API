
import datetime
import re
from json_tricks import dumps
from flask import jsonify
from flask_restful import reqparse, Resource
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_raw_jwt)

# local imports 
from app.bcrypt_instance import Bcrypt
from ..models.auth import UserModel
from ..models.blacklisted import Blacklisted
from ...middleware.middleware import both_roles_allowed, admin_allowed


class SignupResource(Resource):
    """
        Register user endpint
    """
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('confirm_password', type=str, required=True)
    parser.add_argument('email', type=str, required=True)

    @admin_allowed
    def post(self):
        data = SignupResource().parser.parse_args()

        # validations for input
        # eliminate space in username
        username = ''.join(data['username'].split())

        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

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
        if type(user_with_email) is not tuple:
            return {"message": "user with email already registred"}, 409
    
        user.create_user()
        return {"message": "registration sucessfull"}, 201


class LoginResource(Resource):

    """
        Login user endpoint
    """
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    def post(self):
        data = LoginResource.parser.parse_args()

        # validate email

        if not re.match(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                data['email']):
            return {"message": "invalid email"}, 422

        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

        user = UserModel(email=data['email'], password=data['password'])
        user_with_email = user.get_item('users', email=data['email'])
        expires = datetime.timedelta(days=1)
        # check if password match
        if type(user_with_email) is not tuple:
            user_id = user_with_email['user_id']
            role = user_with_email['role']
            if role == 1:
                role_name = "attendant"
            else:
                role_name = "admin"
            if Bcrypt.check_password_hash(user_with_email['password'],
                                          data['password']):
                access_token = create_access_token(identity=(user_id, role), 
                                                   expires_delta=expires)
                return{"access_token": access_token, 
                       "message": "logged in", 
                       "role": role_name}, 200
        return {"message": "invalid credentials"}, 422


class LogoutResource(Resource):
    """
        logout endpoint
    """

    @both_roles_allowed
    def post(self):
        jti = get_raw_jwt()['jti']
        blacklisted = Blacklisted(jti)
        blacklisted.blacklisted()
        return {"message": "logged out"}, 200


class UserRoleResource(Resource):
    """ class contains enpoints to promot user """
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)

    @admin_allowed
    def post(self):
        """ the endpoint to edit roles"""
        data = UserRoleResource.parser.parse_args()

        # validate the inputs 
        if not re.match(
                    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                    data['email']):
            return {"message": "invalid email"}, 422

        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

        # get the user with email
        user = UserModel(email=data['email'])
        user_with_email = user.get_item('users', email=data['email'])

        if type(user_with_email) is not tuple:
            # change role based on current role
            user_role = user_with_email['role']
            if user_role == 2:
                user_role = 1
                message = "role changed to attendant"
            elif user_role == 1:
                user_role = 2
                message = "role changed to admin"
            user.change_role(data['email'], user_role)
            return {"message": message}
