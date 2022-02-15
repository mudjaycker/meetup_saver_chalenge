from models.meetupmodel import MeetupModel
from flask_restx import Resource, fields, Api
from flask import request
from schemas.meetupschemas import MeetupsSchema
from marshmallow import ValidationError
from flask import Blueprint


bp = Blueprint("api", __name__, url_prefix="/api/1")

api = Api(bp, version="1.0", title="Meetup API", description="A simple Meetup API")

_meetup_model = api.model(
    "MeetupSchema",
    {
        "title": fields.String,
        "subtitle": fields.String,
        "address": fields.String,
        "imageurl": fields.String,
        "email": fields.String,
    },
)

_mu_schema = MeetupsSchema()


@api.route("/meetup")
class Meetup(Resource):
    @classmethod
    def get(cls):
        return {"meetups": [_mu_schema.dump(mu) for mu in MeetupModel.find_all()]}
    
    @api.expect(_meetup_model)
    def post(self):
        try:

            meetup = _mu_schema.load(data=request.get_json())
            
            
        except ValidationError as ve:
            return {"message": ve.messages}, 404

        if MeetupModel.find_by_title(meetup.title):
            return {"message": "meetup already exist"}, 403


        meetup.save_to_db()


        return {"message": "saved successfully", "datas": _mu_schema.dump(mu)}

    @api.expect(_meetup_model)
    def put(self):
        try:
            data = _mu_schema.load(data=request.get_json())

        except ValidationError as ve:
            return ve.messages, 404

        if not MeetupModel.find_by_title(data["title"]):
            return {"message": "cannot update unset data"}, 505

        mu = MeetupModel(**data)
        mu.update_to_db(data["title"])
        return {"message": _mu_schema.dump(mu)}


@api.route("/meetup/by/<string:title>")
@api.doc(params={"title": "The title of meetup this must be unique"})
class MeetupModifyDatas(Resource):
    def get(self, title: str):
        mu = MeetupModel.find_by_title(title)

        if not isinstance(mu, str):
            return {"message": "type value not valid expeted string"}, 404

        if mu:
            return {"message": _mu_schema.dump(mu)}

        return {"message": "meetup not found"}

    def delete(self, title):
        mu = MeetupModel.find_by_title(title)

        if mu:
            mu.delete_from_db()
            return {"message": "successfully deleted"}
        return {"message": "error"}, 500
