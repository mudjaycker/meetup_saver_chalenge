from ma import ma
from models.meetupmodel import MeetupModel

class MeetupsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MeetupModel