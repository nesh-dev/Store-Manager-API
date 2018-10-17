import datetime
from flask_restful import reqparse, Resource
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_raw_jwt)
from werkzeug.security import safe_str_cmp
from flask import jsonify

import re

# local imports
from ..models.auth import UserModel
from ..middleware.middleware import attendant_auth, admin_auth


class RegisterResource(Resource):
    """
        Register user endpint
    """
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('confirm_password', type=str, required=True)
    parser.add_argument('role', type=int, required=True)
    parser.add_argument('email', type=str, required=True)

    def post(self):
        data = RegisterResource().parser.parse_args()

        # validations for input
        # eliminate space in username
        username = ''.join(data['username'].split())
        role_id = [1, 2]

        try:
            if not re.match(
                r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                    data['email']):
                return {"message": "invalid email"}, 422
            elif len(data['password']) < 6:
                return {"message":
                        "password should atleast six characters long"}
            elif data['role'] not in role_id:
                return {"message": "role id should either be 1 or 2"}
            elif data['username'] == "":
                return {"message": "username should not be empty"}
            elif data['confirm_password'] != data["password"]:
                return {"message": "passwords do not match"}
        except:
            pass

        # increment Id
        user_id = UserModel.get_length(UserModel.get_users()) + 1

        if UserModel.get_by_name(data['email'], UserModel.get_users()):
            return {"message": "user with email already registred"}, 409

        user_data = {
            "id": user_id, "username": username,
            "email": data["email"], "password": data["password"],
            "role": data["role"]}

        UserModel.add_user((user_data))
        user = UserModel.get_by_id(user_id, UserModel.get_users())
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
        try:
            if not re.match(
                r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                    data['email']):
                return {"message": "invalid email"}, 422
        except:
            pass

        if UserModel.get_length(UserModel.get_users()) == 0:
            return {"message": "please register"}
        # check if user exists
        user = UserModel.get_by_name(data['email'], UserModel.get_users())
        # check if password match
        if user and safe_str_cmp(user['password'], data['password']):
            access_token = create_access_token(identity=user)
        
            return{"access_token": access_token, "message": "logged in"}, 200
        return {"message": "invalid credentials"}, 422


class LogoutResource(Resource):
    """
        logout endpoint
    """

    @attendant_auth
    def post(self):
        jti = get_raw_jwt()['jti']
        blacklisted = UserModel.blacklist(jti)
        return {"message": "logged out"}, 200
