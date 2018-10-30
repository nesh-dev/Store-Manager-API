import os
from flask import Flask
from flask_restful import Api
from config import app_config

# local imports
from .jwt_instance import jwt
from .api.v1 import apiv1
from .api.v2 import apiv2
from .api.v2.views.redirects import docs_blueprint, home_blueprint
from .api.v2.database.database_connection import create_database_tables


def create_app(config_name):
    """
        App initialization
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])

    jwt.init_app(app)

    with app.app_context(): 
        create_database_tables()

    app.register_blueprint(apiv1)
    app.register_blueprint(apiv2)
    app.register_blueprint(docs_blueprint)
    app.register_blueprint(home_blueprint)
    return app
