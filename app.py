from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    school = db.Column(db.String(200))

    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def __repr__(self):
        return '<%r>' % self.name

@app.route('/')
def show_people():
    info = []
    for person in Person.query.all():
        info.append((person.name, person.age, person.school))
    return render_template('index.html', info=info)