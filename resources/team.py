from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models.team import TeamModel
from schemas import TeamSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Teams", "teams", description="Operations on teams")

@blp.route("/team/<string:team_id>")
class Team(MethodView):

    @blp.response(200, TeamSchema)
    def get(self, team_id):
        team = TeamModel.query.get_or_404(team_id)
        return team

    def delete(self, team_id):
        TeamModel.query.get_or_404(team_id)
        raise NotImplementedError("Deleting a team is not implemented.")

@blp.route("/team")
class TeamList(MethodView):
    def get(self):
        return TeamModel.query.all()

    @blp.arguments(TeamSchema)
    @blp.response(201, TeamSchema)
    def post(self, team_data):
        team = TeamModel(**team_data)
        try:
            db.session.add(team)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A team with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the team.")

        return team