from flask import Blueprint
from flask_restful import Api

apiv2 = Blueprint('apiv2', __name__)

api = Api(apiv2, prefix='/api/v2')

