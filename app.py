import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from db import db

import models

from resources.user import blp as UserBlueprint
from resources.time_log import blp as TimeLogBlueprint
from resources.team import blp as TeamBlueprint

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    jwt = JWTManager(app)

    with app.app_context():
        db.create_all() 
        print(os.getenv("DATABASE_URL"))
        print("Banco de dados conectado!")

    api.register_blueprint(UserBlueprint)
    api.register_blueprint(TimeLogBlueprint)
    api.register_blueprint(TeamBlueprint)

    return app