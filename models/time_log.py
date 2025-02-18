from db import db
from datetime import datetime

class TimeLogModel(db.Model):
    __tablename__ = "time_log"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False) 
    schedule = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) 
    status = db.Column(db.String(80), nullable=False) 
 
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'), nullable=True)
    trainer = db.relationship("TrainerModel", back_populates="time_logs", foreign_keys=[trainer_id])

    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=True)
    student = db.relationship("StudentModel", back_populates="time_logs", foreign_keys=[student_id])


