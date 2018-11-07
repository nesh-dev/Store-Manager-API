from flask import Blueprint
from flask_restful import Api
from datetime import date

# local imports  
from .views.auth import (SignupResource, LoginResource, LogoutResource, 
                         UserRoleResource)

from .views.products import (ProductListResource, ProductsResource,
                             SearchProduct)

from .views.sales import SalesListResource, SalesResource, AttendatSales

from .views.category import (CategoryListResource, CategoryResource, 
                             AddProductsToCategories, ProductsInCategory)

from .views.redirects import home, docs 
                  
apiv2 = Blueprint('apiv2', __name__)


api = Api(apiv2, prefix='/api/v2')


api.add_resource(SignupResource, '/auth/signup')
api.add_resource(LoginResource, '/auth/login')
api.add_resource(LogoutResource, '/auth/logout')
api.add_resource(UserRoleResource, '/auth/role')

api.add_resource(ProductListResource, '/products')
api.add_resource(ProductsResource, '/products/<int:id>')

api.add_resource(SalesListResource, '/sales')
api.add_resource(SalesResource, '/sales/<int:id>')
api.add_resource(AttendatSales, '/sales/<string:email>')

api.add_resource(CategoryListResource, '/categories')
api.add_resource(CategoryResource, '/category/<int:id>')
api.add_resource(AddProductsToCategories, '/cat/products')
api.add_resource(ProductsInCategory, '/products/cat/<int:id>')
api.add_resource(SearchProduct, '/search/<string:name>')