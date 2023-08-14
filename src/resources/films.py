from flask_restful import Resource
from flask import request
from typing import List
from src.database.models import Film
from datetime import datetime
from src import db
from src.schemas.films import FilmSchema
from marshmallow.exceptions import ValidationError



class FilmListApi(Resource):
    film_schema = FilmSchema()

    def get(self, uuid=None):
        if not uuid:
            films = db.session.query(Film).all()
            return self.film_schema.dump(films, many=True), 200
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return "", 404
        return self.film_schema.dump(film), 200

        
    def post(self):
        try:
            film = self.film_schema.load(request.json, session=db.session)
        except ValidationError as e:
                return {'message': str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 200

    def put(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return "", 400
        try:
            film = self.film_schema.load(request.json, instance=film, session=db.session)
        except ValidationError as e:
                return {'message': str(e)}, 400
        db.sessiom.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 200


    def patch(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return {'message': 'Wrong data'}, 400
        film_json = request.json
        title=film_json.get('title')
        release_date=datetime.strptime(film_json.get('release_date'), '%B-%m-%Y') if film_json.get('release_date') else None
        distributed_by=film_json.get('distributed_by')
        description=film_json.get('description')
        length=film_json.get('length')
        rating=film_json.get('rating')
        if title:
            film.title = title
        elif release_date:
            film.release_date = release_date
        elif distributed_by:
            film.distributed_by = distributed_by
        elif description:
            film.description = description
        elif length:
            film.length = length
        elif rating:
            film.rating = rating

        db.session.add(film)
        db.session.commit()
        return {'message': 'Created successfully'}, 200
        
    def delete(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return {'message': 'Wrong data'}, 400
        db.session.delete(film)
        db.session.commit()
        return "", 204