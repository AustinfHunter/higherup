from app import db, bcrypt

from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(80))
    user_name = db.Column(db.String(250))
    is_admin = db.Column(db.Boolean)
    create_on = db.Column(db.DateTime)
    desired_job_type = db.Column(db.String)
    is_alum = db.Column(db.Boolean)
    classification_year = db.Column(db.Integer)

    def __init__(self, user_name, email, password, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.is_admin = is_admin
