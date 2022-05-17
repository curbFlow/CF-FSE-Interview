from flask_restful import abort, reqparse, Resource
import sqlalchemy

from ..api.application import api

user_parser = reqparse.RequestParser()
user_parser.add_argument('email')

class User(Resource):
    def get(self, user_id):
        from .. import db # a bit hacky to avoid circ import
        u = db.User.query.get_or_404(user_id)
        return db.user_schema.dump(u)

    def delete(self, user_id):
        from .. import db # a bit hacky to avoid circ import
        u = db.User.query.get_or_404(user_id)
        u.delete()
        db.session.commit()
        return '', 204

class Users(Resource):
    def post(self):
        from .. import db
        args = user_parser.parse_args()
        user = db.User(email=args['email'])
        try:
            db.db.session.add(user)
            db.db.session.commit()
            return db.user_schema.dump(user), 201
        except sqlalchemy.exc.IntegrityError:
            return 'Already exists', 409

api.add_resource(User, '/user/<int:user_id>')
api.add_resource(Users, '/users')

