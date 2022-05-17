from flask_restful import Resource

from ..api.application import api

class Course(Resource):
    def get(self, course_id):
        from .. import db # a bit hacky to avoid circ import
        c = db.Course.query.get_or_404(course_id)
        return db.course_schema.dump(c)

# CourseList
# shows a list of all courses
class Courses(Resource):
    def get(self):
        from .. import db
        courses = db.Course.query.all()
        return db.courses_schema.dump(courses)

api.add_resource(Course, '/course/<int:course_id>')
api.add_resource(Courses, '/courses')
