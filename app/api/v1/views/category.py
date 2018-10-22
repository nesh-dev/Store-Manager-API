
from flask_restful import reqparse, Resource
# local imports
from ..models.category import categoryModel
from ..models.product import productModel
from ...middleware.middleware import (admin_allowed, both_roles_allowed,
                                      attendant_allowed)


# all categories in list
cat_list = categoryModel.get_categories()
product_list = productModel.get_products()


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

    @admin_allowed
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

    @admin_allowed
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

    @admin_allowed
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


class Categoryproducts(Resource):
    """" add products to category

    """

    parser = reqparse.RequestParser()
    parser.add_argument("category_id", type=int, required=True)
    parser.add_argument("product_id", type=int, required=True)

    @attendant_allowed
    def post(self):
        """ add products by getting their id """
        data = Categoryproducts.parser.parse_args()
        product_id = data['product_id']
        category_id = data['category_id']
        product = productModel.get_by_id(product_id, product_list)
        category = categoryModel.get_by_id(category_id, cat_list)
        product_message = "no product with id".format(product_id)
        category_message = "no category with id".format(category_id)

        if category:
            if product:
                product_input = {"product_name": product['name'],
                                 "category_name": category['name']}
                categoryModel.add_products(product_input)
                return product_input, 201
            return {"message": product_message}, 404
        return {"message": category_message}, 404

    def get(self):
        """ get all products in the category category """
        products = categoryModel.get_product_in_cat()
        if not products:
            return {"message": "no products assigned to the category"}, 404
        return products
