from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email =  db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    firstName = db.Column(db.String(80), unique=False, nullable=False)
    lastName = db.Column(db.String(80), unique=False, nullable=False)
    role = db.Column(db.String(80), unique=False, nullable=False)

    team_id = db.Column(
        db.Integer, db.ForeignKey("teams.id"), unique=False, nullable=True
    )
    team = db.relationship("TeamModel", back_populates="users")

    time_logs = db.relationship("TimeLogModel", back_populates="user")