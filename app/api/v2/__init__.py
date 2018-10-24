from flask import Blueprint
from flask_restful import Api

# local imports  
from .views.auth import SignupResource, LoginResource, LogoutResource

apiv2 = Blueprint('apiv2', __name__)

api = Api(apiv2, prefix='/api/v2')


api.add_resource(SignupResource, '/auth/signup')
api.add_resource(LoginResource, '/auth/login')
api.add_resource(LogoutResource, '/auth/logout')