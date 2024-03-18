# Создать базу данных для хранения информации о студентах университета. База данных должна содержать
# две таблицы: "Студенты" и "Факультеты". В таблице "Студенты" должны быть следующие поля: id, имя,
# фамилия, возраст, пол, группа и id факультета. В таблице "Факультеты" должны быть следующие поля:
# id и название факультета. Необходимо создать связь между таблицами "Студенты" и "Факультеты". Написать
# функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.


from flask import Flask, render_template, jsonify
from models_hw import db, Student, Faculty, Gender
from random import choice, randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_001.db'
db.init_app(app)


@app.route('/')
def start():
    return 'Hi!'


@app.route('/students/')
def students():
    students = db.session.query(Student).all()
    return render_template('students.html', student=students)


@app.route('/students/group/<int:group>/')
def get_students_by_group(group):
    student = Student.query.filter_by(group=group).all()
    if students:
        return jsonify(
            [{'name': student.name, 'last-name': student.last_name, 'group': student.group,
              'faculty': student.faculty_id} for student in student])
    else:
        return jsonify({'error': 'Student not found'}), 404


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Ok')


@app.cli.command('fill-db')
def fill_db():
    count = 10
    for student in range(1, count + 1):
        new_student = Student(
            name=f'student{student}',
            last_name=f'last_name{student}',
            age=choice([student*5, 60]),
            gender=choice([Gender.male, Gender.female]),
            group=randint(1, 11),
            faculty_id=randint(1, 10)
        )
        db.session.add(new_student)
    db.session.commit()

    for faculty in range(1, count):
        new_faculty = Faculty(faculty_name=f'faculty{faculty}')
        db.session.add(new_faculty)
    db.session.commit()
    print('Ok2')


if __name__ == '__main__':
    app.run(debug=True)
