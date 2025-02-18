from db import db

class StudentModel(db.model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    email =  db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    firstName = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)

    trainer_id = db.Column(
        db.Integer, db.ForeignKey("trainers.id"), unique=False, nullable=False
    )
    trainer = db.relationship("TrainerModel", back_populates="students")

    time_logs = db.relationship("TimeLogModel", back_populates="student")