import logging
from flask import Flask, jsonify, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField
from pprint import pprint
from utils.email_client import send_email

app = Flask(__name__, static_folder='static/assets')
# logging.basicConfig(filename='email_client.log',level=logging.DEBUG,
#                     format='%(asctime)s %(message)s')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hacktech'
db = SQLAlchemy(app)

class User(db.Model):
    #TODO: finish this
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(120))
    lname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, fname, lname, email):
        '''
        initialize the user database.
        things that should be stored:
        first name, last name, school, grade
        transportation, which bus if any
        interested in: web dev, mobile dev, AR/VR, hardware, AI/ML, other
        resume file
        links to github, linkedin, portfolio
        over 18 by march 3, 2017?
        acrostic poem based around the word "ROSE"
        something you did today that could have been enhanced by tech
        cool things you'd like to see at hacktech
        questions/comments/concerns
        do you accept MLH code of conduct?
        '''
        self.fname = fname
        self.lname = lname
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
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():

    form = RegistrationForm(request.form)
    user = User(form.fname.data, form.lname.data, form.email.data)
    # Now we'll send the email application confirmation
    subject = "Thanks for Applying to Hacktech 2017!"
    html = render_template('Hacktech2017_submitapplication.html')
    send_email(user.email, subject, html)

    #TODO: finish this
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.fname.data, form.lname.data, form.email.data)
        db.session.add(user)
        db.session.commit()

        return "Thank you for registering, "+form.fname.data+"."
    elif request.method == 'POST':
        return "There was a problem with your registration information.\nPlease check your information and try again."
    return render_template('register.html', form=form)

@app.route('/data')
def names():
    data = []
    for user in User.query.all():
        data.append((user.fname, user.lname, user.email))
    pprint(data)
    return 'ok'

if __name__ == '__main__':
    app.run()
