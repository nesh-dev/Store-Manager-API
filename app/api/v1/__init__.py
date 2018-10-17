from flask import Blueprint 

from flask_restful import Api 


apiv1 = Blueprint('apiv1', __name__)

api1 = Api(apiv1, prefix='/apiv1/v2')


