from db import db

class TeamModel(db.model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    email =  db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    firstName = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)

    users = db.relationship("UserModel", back_populates="team", lazy="dynamic")

    time_logs = db.relationship("TimeLogModel", back_populates="team")


