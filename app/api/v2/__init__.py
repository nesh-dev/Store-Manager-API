from flask import Blueprint


apiv1 = Blueprint('apiv1', __name__)

api = Api(apiv1, prefix='/api/v2')

