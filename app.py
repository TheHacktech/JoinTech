from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static/assets')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hacktech'
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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def names():
    data = {"names": ["Jhen", "Jandrew", "Jrace", "Jenny", "Jeng", "Jadvith"]}
    return jsonify(data)


if __name__ == '__main__':
    app.run()

