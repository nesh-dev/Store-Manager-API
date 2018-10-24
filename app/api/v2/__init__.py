from flask import Blueprint
from flask_restful import Api
from datetime import date

# local imports  
from .views.auth import (SignupResource, LoginResource, LogoutResource, 
                         UserRoleResource)
                  
apiv2 = Blueprint('apiv2', __name__)


api = Api(apiv2, prefix='/api/v2')


api.add_resource(SignupResource, '/auth/signup')
api.add_resource(LoginResource, '/auth/login')
api.add_resource(LogoutResource, '/auth/logout')
api.add_resource(UserRoleResource, '/auth/role')