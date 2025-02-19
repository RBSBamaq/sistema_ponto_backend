from marshmallow import Schema, fields

class PlainTeamSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    password = fields.Str(load_only=True) 
    firstName = fields.Str(required=True)
    lastName = fields.Str(required=True)
    role = fields.Str(required=True)

class PlainTimeLogSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Str(required=True)
    schedule = fields.DateTime()
    team_id = fields.Int(dump_only=True)
    user_id = fields.Int(dump_only=True)

class TeamSchema(PlainTeamSchema):
    users = fields.List(fields.Nested(PlainUserSchema), dump_only=True)
    time_logs = fields.List(fields.Nested(PlainTimeLogSchema), dump_only=True)

class UserSchema(PlainUserSchema):
    team_id = fields.Int(required=False, load_only=True)
    team = fields.Nested(PlainTeamSchema, dump_only=True)
    time_logs = fields.List(fields.Nested(PlainTimeLogSchema), dump_only=True)

class TimeLogSchema(PlainTimeLogSchema):
    team = fields.Nested(PlainTeamSchema, dump_only=True)
    user = fields.Nested(PlainUserSchema, dump_only=True)
