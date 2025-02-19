from db import db
from datetime import datetime

class TimeLogModel(db.Model):
    __tablename__ = "time_log"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False) 
    schedule = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) 
    status = db.Column(db.String(80), nullable=False) 
 
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)
    team = db.relationship("TeamModel", back_populates="time_logs", foreign_keys=[team_id])

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    user = db.relationship("UserModel", back_populates="time_logs", foreign_keys=[user_id])


