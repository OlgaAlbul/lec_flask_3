# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.

from flask import Flask, render_template
from models_hw3 import db, Students, Grades
from random import choice, randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_003.db'
db.init_app(app)


@app.route('/')
def start():
    return 'Hi!'


@app.route('/all-students-grades/')
def all_students_grades():
    all_students_grades = db.session.query(Grades).all()
    return render_template('all_students_grades.html', grades=all_students_grades)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Ok')


@app.cli.command('fill-db')
def fill_db():
    count = 15
    for st in range(1, count + 1):
        new_student = Students(
            st_name=f'Student{st}',
            st_last_name=f'Last_student{st}',
            st_group=randint(1, 11),
            st_email=f'Student{st}@mail.ru',
        )
        db.session.add(new_student)
    db.session.commit()

    for grade in range(1, count + 1):
        new_grade = Grades(
            subject_name=f'Subject{grade}',
            grade=randint(1, 6),
            student_id=randint(1, count)
        )
        db.session.add(new_grade)
    db.session.commit()
    print('Ok2')


if __name__ == '__main__':
    app.run(debug=True)
