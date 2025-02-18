from marshmallow import Schema, fields

class PlainTrainerSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    password = fields.Str(load_only=True)  
    firstName = fields.Str(required=True)
    lastName = fields.Str(required=True)

class PlainStudentSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    password = fields.Str(load_only=True) 
    firstName = fields.Str(required=True)
    lastName = fields.Str(required=True)

class PlainTimeLogSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Str(required=True)
    schedule = fields.DateTime()
    trainer_id = fields.Int(dump_only=True)
    student_id = fields.Int(dump_only=True)

class TrainerSchema(PlainTrainerSchema):
    students = fields.List(fields.Nested(PlainStudentSchema), dump_only=True)
    time_logs = fields.List(fields.Nested(PlainTimeLogSchema), dump_only=True)

class StudentSchema(PlainStudentSchema):
    trainer_id = fields.Int(required=True, load_only=True)
    trainer = fields.Nested(PlainTrainerSchema, dump_only=True)
    time_logs = fields.List(fields.Nested(PlainTimeLogSchema), dump_only=True)

class TimeLogSchema(PlainTimeLogSchema):
    trainer = fields.Nested(PlainTrainerSchema, dump_only=True)
    student = fields.Nested(PlainStudentSchema, dump_only=True)
