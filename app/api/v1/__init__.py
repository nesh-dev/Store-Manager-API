
from flask import Blueprint 
from flask_restful import Api 

from .views.auth import RegisterResource, LoginResource, LogoutResource
from .views.products import ProductListResource, ProductResource

from .views.auth import (RegisterResource, LoginResource, 
                         LogoutResource)
from .views.category import CategoryListResource, CategoryResource

from .views.sales import SalesListResource

apiv1 = Blueprint('apiv1', __name__)

api = Api(apiv1, prefix='/api/v1')

# register resources

api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')
api.add_resource(LogoutResource, '/logout')

api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<int:id>')

api.add_resource(CategoryListResource, '/categories')
api.add_resource(CategoryResource, '/category/<int:id>')

api.add_resource(SalesListResource, '/sales')


