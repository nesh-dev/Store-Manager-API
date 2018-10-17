from flask_restful import reqparse, Resource

# local imports 
from ..models.category import CategoryModel
from ..middleware.middleware import attendant_auth, admin_auth


class CategoryListResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("description", type=str, required=True)

    @attendant_auth
    def get(self):
        """
            Return category list
        """
        cat_list = CategoryModel.get_categories()
        return cat_list

    @attendant_auth
    def post(self):
        """
            post an item
        """
        cat_list = CategoryModel.get_categories()
        data = CategoryListResource.parser.parse_args()
        cat_id = len(cat_list) + 1
        if CategoryModel.get_by_name(data['name'], cat_list):
            return {"message": "category with name already exist"}, 409

        category_input = {"id":cat_id, "name": data["name"], 
                          "description": data["description"]}
        CategoryModel.add_category(category_input)
        category = CategoryModel.get_by_name(data['name'], cat_list)
        return category, 201


class CategoryResource(Resource):

    @attendant_auth
    def get(self, id):
        """
            get by id
        """
        message = "category with id {} does not exist".format(id)
        cat_list = CategoryModel.get_categories()
        category = CategoryModel.get_by_id(id, cat_list)
        if category:
            return category, 200
        return {"message": message}, 404

    
