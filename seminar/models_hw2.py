from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Authors(db.Model):
    au_id = db.Column(db.Integer, primary_key=True)
    au_name = db.Column(db.String(80), nullable=False)
    au_last_name = db.Column(db.String(80), nullable=False)
    book = db.relationship('Books', backref=db.backref(f'authors'), lazy=True)

    def __repr__(self):
        return f' {Authors.au_name} {Authors.au_last_name}'


class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(120), unique=True, nullable=False)
    book_year = db.Column(db.Integer, nullable=False)
    book_count = db.Column(db.Integer)
    book_auth_id = db.Column(db.Integer, db.ForeignKey('authors.au_id'), nullable=False)

    def __repr__(self):
        return f'Book_name: {self.book_name}, book_year: {self.book_year}, book author: {self.book_auth_id}'
