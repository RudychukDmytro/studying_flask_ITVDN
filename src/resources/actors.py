from flask_restful import Resource
from flask import request
from typing import List
from src.database.models import Actor
from datetime import datetime
from src import db
from src.schemas.actors import ActorsSchema
from marshmallow.exceptions import ValidationError


class ActorListApi(Resource):
    actor_schema = ActorsSchema()

    def get(self, id=None):
        if not id:
            actors = db.session.query(Actor).all()
            return self.actor_schema.dump(actors, many=True), 200
        actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return "", 404
        return self.actor_schema.dump(actor), 200

        
    def post(self):
        try:
            actor = self.actor_schema.load(request.json, session=db.session)
        except ValidationError as e:
                return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass