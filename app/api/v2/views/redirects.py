from flask import redirect, jsonify
from flask import Blueprint


home_blueprint = Blueprint('home', __name__)
docs_blueprint = Blueprint('docs', __name__)

@docs_blueprint.route('/docs')
def docs():
    return redirect('https://storemanagerv2.docs.apiary.io')


@home_blueprint.route('/')
def home():
    return jsonify({"mesage": "welcome to Store Manager API"})
