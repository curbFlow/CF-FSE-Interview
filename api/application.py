from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from .config import env_config

api = Api()

db = SQLAlchemy()

ma = Marshmallow()

def create_app(config_name):
    #import our resource folder to avoid circular 
    #dependency error
    from .. import resources

    app = Flask(__name__)

    app.config.from_object(env_config[config_name])
    api.init_app(app)
    
    db.init_app(app)

    ma.init_app(app)

    return app
