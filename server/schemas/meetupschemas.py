from marshmallow import Schema, fields

class MeetupsSchema(Schema):
    title = fields.Str(required=True)
    subtitle = fields.Str(required=True)
    address = fields.Str(required=True)
    imageurl = fields.Str(required=True)
    email = fields.Str(required=True)