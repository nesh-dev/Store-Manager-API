from flask_restful import reqparse, Resource
from flask_jwt_extended import (create_access_token, create_refresh_token)

from ..models.auth import UserModel


class RegisterResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('role', type=int, required=True)

    def post(self):
        data = RegisterResource().parser.parse_args()
        user_id = UserModel.get_length(UserModel.get_users()) + 1

        if UserModel.get_by_name(data['email'], UserModel.get_users()):
            return {"message": "user with email already registred"}
        user_data = {
            "id": user_id, "username": data["username"],
            "email": data["email"], "password": data["password"],
            "role": data["role"]}

        UserModel.add_user(user_data)
        user = UserModel.get_by_id(user_id, UserModel.get_users())
        return user
