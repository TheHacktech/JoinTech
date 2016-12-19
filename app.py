from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField

app = Flask(__name__, static_folder='static/assets')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hacktech'
db = SQLAlchemy(app)

class User(db.Model):
    #TODO: finish this
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(120))
    lname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class RegistrationForm(Form):
    fname = StringField('First Name', [validators.Length(min=1, max=120), validators.DataRequired()])
    lname = StringField('Last Name', [validators.Length(min=1, max=120), validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=6, max=120), validators.Email(), validators.DataRequired()])
    age = IntegerField('Age', [validators.DataRequired()])
    grade = StringField('Grade', [validators.DataRequired()])
    school = StringField('School/University', [validators.DataRequired()])
    busorigin = StringField('Bus Origin')
    website = StringField('Website')
    linkedin = StringField('LinkedIn Profile')
    #accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    #TODO: finish this
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.fname.data, form.lname.data, form.email.data,
        #            form.password.data)
        #db_session.add(user)
        return "Thank you for registering, "+form.fname.data+"."
    elif request.method == 'POST':
        return "There was a problem with your registration information.\nPlease check your information and try again."
    return render_template('register.html', form=form)

@app.route('/data')
def names():
    data = {"names": ["Jhen", "Jandrew", "Jrace", "Jenny", "Jeng", "Jadvith"]}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
