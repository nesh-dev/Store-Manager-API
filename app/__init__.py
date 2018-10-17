import os 
from flask import Flask 
from flask_restful import Api
from instance.config import app_config

from .jwt import jwt


def create_app(config_name):
    """
        App initialization
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    jwt.init_app(app)
    return app