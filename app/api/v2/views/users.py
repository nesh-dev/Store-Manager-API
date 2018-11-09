from flask import jsonify
from flask_restful import reqparse, Resource

from ...middleware.middleware import both_roles_allowed, admin_allowed
from ..models.auth import UserModel


class UserListResource(Resource): 

    def get(self):
        user = UserModel()
        users = user.get_all('users')
        users_list = []
        for user in users:
        	name = user['user_name']
        	email = user['email']
        	role = user['role']
        	each_user = {"name":name, "email":email, "role":role}
        	users_list.append(each_user)
        return users_list


class UserResource(Resource):
    def delete(self, id):
        user = UserModel()
        user_to_delete = user.get_item('users', user_id=id)
        message = "user with id {} does not exist".format(id)
        if user_to_delete:
        	user.delete('users', user_id=id)
        	return {"message": "user deleted"}, 202
        return {"message": message}