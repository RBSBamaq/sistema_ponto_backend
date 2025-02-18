from db import db

class TrainerModel(db.model):
    __tablename__ = "trainers"

    id = db.Column(db.Integer, primary_key=True)
    email =  db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    firstName = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)

    students = db.relationship("StudentModel", back_populates="trainer", lazy="dynamic")


