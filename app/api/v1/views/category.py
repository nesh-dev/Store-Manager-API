
from flask_restful import reqparse, Resource
# local imports
from ..models.category import categoryModel
from ..middleware.middleware import both_roles_allowed


# all categories in list
cat_list = categoryModel.get_categories()


class CategoryListResource(Resource):
    """
        Categories get all and post
    """

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True)
    parser.add_argument("description", type=str, required=True)

    @both_roles_allowed
    def get(self):
        """
            Return category list
        """
        if not cat_list:
            return {"message": "no category saved"}, 404
        return cat_list

    @both_roles_allowed
    def post(self):
        """
            post a category takes name
            and description of category
            both attendat and admin can access
        """

        data = CategoryListResource.parser.parse_args()
        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

        cat_id = len(cat_list) + 1
        if categoryModel.get_by_name(data['name'], cat_list):
            return {"message": "category with name already exist"}, 409

        category_input = {"id": cat_id, "name": data["name"],
                          "description": data["description"]}
        categoryModel.add_category(category_input)
        category = categoryModel.get_by_name(data['name'], cat_list)
        return category, 201


class CategoryResource(Resource):
    """
        Handles requests that require id
    """

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str)
    parser.add_argument("description", type=str)

    @both_roles_allowed
    def get(self, id):
        """
            get the category by its id
        """
        message = "category with id {} does not exist".format(id)
        category = categoryModel.get_by_id(id, cat_list)
        if category:
            return category, 200
        return {"message": message}, 404


    @both_roles_allowed
    def put(self, id):
        """
            edit a category
            get category to edit
            manipulate its data
            both attendat and admin can access
        """

        # validate empty string inputs
        data = CategoryResource.parser.parse_args()
        for k, v in data.items():
            if v == "":
                return {"message": "{} cannot be an empty".format(k)}

        message = "category with id {} does not exist".format(id)
        item_to_edit = categoryModel.get_by_id(id, cat_list)
        if item_to_edit:
            item_to_edit.update(data)
            return item_to_edit, 201
        return {"message": message}, 404

    @both_roles_allowed
    def delete(self, id):
        """
            delete an a category by getting its id
        """
        message = "category with id {} does not exist".format(id)
        item_to_delete = categoryModel.get_by_id(id, cat_list)
        if item_to_delete:
            categoryModel.delete(id, cat_list)
            return {"message": "category deleted"}, 202
        return {"message": message}
