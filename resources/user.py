from db import db
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from models import UserModel
from schemas import UserSchema

blp = Blueprint("users", "users", description="Operations on users")


@blp.route("/user/<string:user_id>")
class user(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel
        UserModel.query.get_or_404(user_id)
        return user
    
    @blp.arguments(UserSchema)
    def put(self, user_id):
        UserModel.query.get_or_404(user_id)
        raise NotImplementedError("Updating an User is not implemented.")
    
    def delete(self, user_id):
        UserModel.query.get_or_404(user_id)
        raise NotImplementedError("Deleting an User is not implemented.")
 


@blp.route("/user")
class userList(MethodView):
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, User_data):
        user = UserModel(**User_data)

        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the User.")

        return user