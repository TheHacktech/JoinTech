from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/hacktech'
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Save e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()


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