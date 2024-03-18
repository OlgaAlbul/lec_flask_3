# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask import Flask, render_template, jsonify
from models_hw2 import db, Books, Authors
from random import choice, randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_002.db'
db.init_app(app)


@app.route('/')
def start():
    return 'Hi!'


@app.route('/all-books/')
def all_books():
    all_books = db.session.query(Books).all()
    return render_template('all_books.html', books=all_books)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Ok')


@app.cli.command('fill-db')
def fill_db():
    count = 15
    for book in range(1, count + 1):
        new_book = Books(
            book_name=f'Book{book}',
            book_year=randint(1700, 2024),
            book_count=randint(1, 51),
            book_auth_id=randint(1,5),
        )
        db.session.add(new_book)
    db.session.commit()

    for author in range(1, 5):
        new_author = Authors(au_name=f'Name{author}', au_last_name=f'Lastname{author}')
        db.session.add(new_author)
    db.session.commit()
    print('Ok2')


if __name__ == '__main__':
    app.run(debug=True)