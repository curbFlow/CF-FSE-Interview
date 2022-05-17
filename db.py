import click

from .api.application import db, ma
from .main import app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),
        nullable=True)
    course = db.relationship('Course',
        backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.email

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "course_id")
        model = User

user_schema = UserSchema()

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Course %r>' % self.title

class CourseSchema(ma.Schema):
    class Meta:
        fields = ("id", "title")
        model = Course

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),
        nullable=True)
    course = db.relationship('Course',
        backref=db.backref('videos', lazy=True))

    def __repr__(self):
        return '<Video %r>' % self.title

@app.cli.command("create-database")
def create_database():
    db.create_all()

