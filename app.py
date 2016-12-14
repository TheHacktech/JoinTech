from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/hacktech'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

# # from flask import Flask, render_template
# # from flask_sqlalchemy import SQLAlchemy

# # app = Flask(__name__)
# # app.config.from_pyfile('config.py')
# # db = SQLAlchemy(app)

# # class Person(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(80), unique=True)
# #     age = db.Column(db.Integer)
# #     school = db.Column(db.String(200))

# #     def __init__(self, name, age, school):
# #         self.name = name
# #         self.age = age
# #         self.school = school

# #     def __repr__(self):
# #         return '<%r>' % self.name

# # @app.route('/')
# # def show_people():
# #     info = []
# #     for person in Person.query.all():
# #         info.append((person.name, person.age, person.school))
# #     return render_template('index.html', info=info)



# from flask import Flask, jsonify

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return 'Flask is running!'


# @app.route('/data')
# def names():
#     data = {"names": ["Jhen", "Jandrew", "Jrace", "Jenny"]}
#     return jsonify(data)


# if __name__ == '__main__':
#     app.run()