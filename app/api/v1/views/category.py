from flask_restful import reqparse, Resource
import re
# local imports
from ..models.category import CategoryModel
from ..middleware.middleware import both_roles_allowed


# all categories in list
cat_list = CategoryModel.get_categories()


class CategoryListResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("description", type=str, required=True)

    @both_roles_allowed
    def get(self):
        """
            Return category list
        """
        cat_list = CategoryModel.get_categories()
        if CategoryModel.get_length(cat_list) == 0:
            return {"message": "no category saved"}, 404
        return cat_list

    @both_roles_allowed
    def post(self):
        """
            post an item
        """

        data = CategoryListResource.parser.parse_args()
        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

        cat_id = len(cat_list) + 1
        if CategoryModel.get_by_name(data['name'], cat_list):
            return {"message": "category with name already exist"}, 409

        category_input = {"id": cat_id, "name": data["name"],
                          "description": data["description"]}
        CategoryModel.add_category(category_input)
        category = CategoryModel.get_by_name(data['name'], cat_list)
        return category, 201


class CategoryResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str)
    parser.add_argument("description", type=str)

    @both_roles_allowed
    def get(self, id):
        """
            get by id
        """
        message = "category with id {} does not exist".format(id)
        category = CategoryModel.get_by_id(id, cat_list)
        if category:
            return category, 200
        return {"message": message}, 404

    @both_roles_allowed
    def put(self, id):
        """
            edit the category
        """

        # validate empty string inputs
        data = CategoryResource.parser.parse_args()
        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

        message = "category with id {} does not exist".format(id)
        item_to_edit = CategoryModel.get_by_id(id, cat_list)
        if item_to_edit:
            item_to_edit.update(data)
            return item_to_edit, 201
        return {"message": message}, 404

    @both_roles_allowed
    def delete(self, id):
        message = "category with id {} does not exist".format(id)
        length = CategoryModel.get_length(cat_list)
        excepted_length = length - 1
        item_to_delete = CategoryModel.get_by_id(id, cat_list)
        if item_to_delete:
            CategoryModel.delete(id, cat_list)
            return {"message": "category deleted"}, 202
        return {"message": message}
