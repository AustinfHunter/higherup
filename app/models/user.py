from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(80))
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
