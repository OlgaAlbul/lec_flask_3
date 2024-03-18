from flask import Flask
from models_05 import db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
db.init_app(app)


@app.route("/")
def index():
    return 'Hi!'


@app.cli.command('init-db')
def init_db():
    # показать ошибку с неверным wsgi.py
    db.create_all()
    print('OK')


@app.cli.command('add-john')
def add_user():
    user = User(username="John", email="john@gmail.com")
    db.session.add(user)
    db.session.commit()
    print('John added successfully!')


@app.cli.command('edit-john')
def edit_user():
    user = User.query.filter_by(username="John").first()
    user.email = "new_email@ex.com"
    db.session.commit()
    print('John edited mail successfully!')


@app.cli.command('del-john')
def del_user():
    user = User.query.filter_by(username="John").first()
    db.session.delete(user)
    db.session.commit()
    print('John deleted successfully!')


if __name__ == '__main__':
    app.run(debug=True)