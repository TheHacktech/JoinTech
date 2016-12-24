from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField
from pprint import pprint

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
    grade = db.Column(db.String(40))
    school = db.Column(db.String(120))
    busorigin = db.Column(db.String(80))
    website = db.Column(db.String(80))
    linkedin = db.Column(db.String(80))

    def __init__(self, fname, lname, email, grade, school, busorigin, website, linkedin):
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
        self.fname     = fname
        self.lname     = lname
        self.email     = email
        self.grade     = grade
        self.school    = school
        self.busorigin = busorigin
        self.website   = website
        self.linkedin  = linkedin

    def __repr__(self):
        return self.fname + ' ' + self.lname + ' ' + self.email + ' ' + self.grade + ' ' + self.school + ' ' + self.busorigin + ' ' + self.website + ' ' + self.linkedin

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
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    #TODO: finish this
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.fname.data, form.lname.data, form.email.data, form.grade.data, form.school.data, form.busorigin.data, form.website.data, form.linkedin.data)
        db.session.add(user)
        db.session.commit()
        return "Thank you for registering, "+form.fname.data+"."
    elif request.method == 'POST':
        return "There was a problem with your registration information.\nPlease check your information and try again."
    return render_template('register.html', form=form)

@app.route('/data')
def names():
    '''this is all useless for now. pls to ignore'''
    data = []
    for user in User.query.all():
        data.append((user.fname, user.lname, user.email))
    pprint(data)
    return 'ok'


if __name__ == '__main__':
    app.run()
