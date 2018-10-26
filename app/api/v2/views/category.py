from flask_restful import reqparse, Resource

from ...middleware.middleware import admin_allowed, both_roles_allowed, attendant_allowed
from ..models.category import CategoryModel


class CategoryListResource(Resource):
    """ categorys list resource"""
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("description", type=str, required=True)
 
    @admin_allowed
    def post(self): 
        """ save categorys """
        data = CategoryListResource.parser.parse_args()

        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}
    
        name = data['name']
        description = data['description']
        category = CategoryModel(name=name, description=description)
        category_with_name = category.get_item('categories', name=name)

        # if item exists a tuple with message and error is returned
        if type(category_with_name) is tuple:
            return category.create_category(), 201
        return {"message": "category with name already exist"}, 409

    @both_roles_allowed
    def get(self):
        category = CategoryModel()
        return category.get_all('categories')


class CategoryResource(Resource):
    """ has endpoints for edit, get and delete"""
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("description", type=str, required=True)

    @both_roles_allowed
    def get(self, id):
        """get a category by id """
        category = CategoryModel()
        category_to_get = category.get_item('categories', category_id=id)
        message = "Category with id {} does not exist".format(id)
        if category_to_get:
            return category_to_get
        return {"message": message}, 404

    @admin_allowed
    def put(self, id):
        
        """update a category """
        data = CategoryResource.parser.parse_args()
        # validate inputs
        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

        name = data['name']
        description = data['description']
        message = "category with id {} does not exist".format(id)
        category = CategoryModel(name=name, description=description)
        category_to_update = category.get_item('categories', category_id=id)
        # import pdb; pdb.set_trace()
        if type(category_to_update) is not tuple:
            return category.update_category(id), 201
        return {"message": message}, 404

    @admin_allowed
    def delete(self, id):
        category = CategoryModel()
        category_to_delete = category.get_item('categories', category_id=id)
        message = "Product with id {} does not exist".format(id)
        if category_to_delete:
            category.delete('categories', category_id=id)
            return {"message": "Category deleted"}, 202
        return {"message": message}


class AddProductsToCategories(Resource):
    """ add  categorys to categories """
    parser = reqparse.RequestParser()
    parser.add_argument("product_id", type=int, required=True)
    parser.add_argument("category_id", type=int, required=True)

    @attendant_allowed
    def post(self):
        data = AddProductsToCategories.parser.parse_args()
        category = CategoryModel()
        return category.add_products(data['category_id'], data['product_id'])


class ProductsInCategory(Resource):
    """ get items in category """
    @both_roles_allowed
    def get(get, id):
        category = CategoryModel()
        return category.get_all_with('category_items', category_id=id)
