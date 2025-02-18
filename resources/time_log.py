from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import TimeLogModel
from schemas import TimeLogSchema

blp = Blueprint("time_logs", "time_logs", description="Operations on time logs")

@blp.route("/time_log")
class TimeLogList(MethodView):
    @blp.response(200, TimeLogSchema(many=True))
    def get(self):
        return TimeLogModel.query.all()

    @blp.arguments(TimeLogSchema)
    @blp.response(201, TimeLogSchema)
    def post(self, time_log_data):
        time_log = TimeLogModel(**time_log_data)

        try:
            db.session.add(time_log)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the time log.")

        return time_log
