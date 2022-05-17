import click

from .api.application import db
from .main import app
from .db import User, Course, Video

@app.cli.command("add-model-data")
def create_sample_data():
    # Courses
    cv = Course(title='Intro to Computer Vision')
    db.session.add(cv)
    py = Course(title='Intro to Python')
    db.session.add(py)    

    db.session.add_all([
        # Videos
        Video(title='Hough Transforms', course=cv, position=0),
        Video(title='Camera Corrections', course=cv, position=1),
        Video(title='ResNet', course=cv, position=2),
        Video(title='YOLO', course=cv, position=3),
        Video(title='Variables', course=py, position=0),
        Video(title='Expressions', course=py, position=1),
        Video(title='Statements', course=py, position=2),
        Video(title='Control Flow', course=py, position=3),

        # Users
        User(email='jill.jones@curbflow.com', course=cv),
        User(email='david.davison@curbflow.com', course=py),
    ])

    db.session.commit()
