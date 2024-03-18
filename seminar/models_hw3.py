from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Students(db.Model):
    st_id = db.Column(db.Integer, primary_key=True)
    st_name = db.Column(db.String(80), nullable=False)
    st_last_name = db.Column(db.String(120), nullable=False)
    st_group = db.Column(db.Integer, nullable=False)
    st_email = db.Column(db.String(80), nullable=False)
    grade = db.relationship('Grades', backref=db.backref(f'students'), lazy=True)

    def __repr__(self):
        return f'Student({self.name}, {self.last_name}, {self.fac_name})'


class Grades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(80), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.st_id'), nullable=False)
    grade = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Student{self.student_id} have grade {self.grade} on subject {self.subject_name})'
