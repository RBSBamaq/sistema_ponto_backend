from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models.trainer import TrainerModel
from schemas import TrainerSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Trainers", "trainers", description="Operations on trainers")

@blp.route("/trainer/<string:trainer_id>")
class Trainer(MethodView):

    @blp.response(200, TrainerSchema)
    def get(self, trainer_id):
        trainer = TrainerModel.query.get_or_404(trainer_id)
        return trainer

    def delete(self, trainer_id):
        TrainerModel.query.get_or_404(trainer_id)
        raise NotImplementedError("Deleting a trainer is not implemented.")

@blp.route("/trainer")
class TrainerList(MethodView):
    def get(self):
        return TrainerModel.query.all()

    @blp.arguments(TrainerSchema)
    @blp.response(201, TrainerSchema)
    def post(self, trainer_data):
        trainer = TrainerModel(**trainer_data)
        try:
            db.session.add(trainer)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A trainer with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the trainer.")

        return trainer