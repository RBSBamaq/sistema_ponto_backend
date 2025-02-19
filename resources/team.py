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

   