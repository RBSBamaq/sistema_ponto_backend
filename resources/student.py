from db import db
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from models import StudentModel
from schemas import StudentSchema

blp = Blueprint("students", "students", description="Operations on students")


@blp.route("/student/<string:student_id>")
class student(MethodView):
    @blp.response(200, StudentSchema)
    def get(self, student_id):
        student = StudentModel
        StudentModel.query.get_or_404(student_id)
        return student
    
    @blp.arguments(StudentSchema)
    def put(self, student_id):
        StudentModel.query.get_or_404(student_id)
        raise NotImplementedError("Updating an Student is not implemented.")
    
    def delete(self, student_id):
        StudentModel.query.get_or_404(student_id)
        raise NotImplementedError("Deleting an Student is not implemented.")
 


@blp.route("/student")
class studentList(MethodView):
    def get(self):
        return StudentModel.query.all()

    @blp.arguments(StudentSchema)
    @blp.response(201, StudentSchema)
    def post(self, Student_data):
        student = StudentModel(**Student_data)

        try:
            db.session.add(student)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the Student.")

        return student