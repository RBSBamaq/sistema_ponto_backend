from db import db
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

from models import UserModel
from models.team import TeamModel
from schemas import UserSchema

blp = Blueprint("users", "users", description="Operations on users")


@blp.route("/user/<string:user_id>")

class User(MethodView):
    @jwt_required()
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
class UserList(MethodView):
    @jwt_required()
    def get(self):
        return UserModel.query.all()

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.email == user_data["email"]).first():
            abort(409, message="A user with that email already exists.")

        user = UserModel(
            email=user_data["email"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
        db.session.add(user)
        db.session.flush()

        if user.role.lower() == "líder":  
            team = TeamModel(name=f"Team {user.firstName}", leader_id=user.id)
            db.session.add(team)
            db.session.flush()

            user.team_id = team.id

        db.session.commit()

        return {"message": "User created successfully."}, 201

@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.email == user_data["email"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=str(user.id))
            return {"access_token": access_token}, 200

        abort(401, message="Invalid credentials.")