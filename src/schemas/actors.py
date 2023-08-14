from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.database.models import Actor

class ActorsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actor
        load_instance = True