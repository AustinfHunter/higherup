from app import db, bcrypt

from flask_login import UserMixin

# These imports are not used directly
# but are required for sqlalchemy to create join tables
from app.models.jobtype import JobType
from app.models.skill import Skill
from app.models.topic import Topic
from app.models.company import Company

user_job_type = db.Table(
    'user_job_type',
    db.Column('user_id',
              db.Integer,
              db.ForeignKey('user.id')
              ),
    db.Column('job_type_id',
              db.Integer,
              db.ForeignKey('job_type.id')
              )
)

user_topic = db.Table(
    'user_topic',
    db.Column('user_id',
              db.Integer,
              db.ForeignKey('user.id')
              ),
    db.Column('topic_id',
              db.Integer,
              db.ForeignKey('topic.id')
              )
)

user_skill = db.Table(
    'user_skill',
    db.Column('user_id',
              db.Integer,
              db.ForeignKey('user.id')
              ),
    db.Column('skill_id',
              db.Integer,
              db.ForeignKey('skill.id')
              )
)

user_company = db.Table(
    'user_company',
    db.Column('user_id',
              db.Integer,
              db.ForeignKey('user.id')
              ),
    db.Column('company_id',
              db.Integer,
              db.ForeignKey('company.id')
              )
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(80))
    user_name = db.Column(db.String(250))
    is_admin = db.Column(db.Boolean)
    create_on = db.Column(db.DateTime)
    is_alum = db.Column(db.Boolean)
    classification_year = db.Column(db.Integer)
    skills = db.relationship(
        'Skill',
        secondary=user_skill,
        backref='skill')
    topics = db.relationship(
        'Topic',
        secondary=user_topic,
        backref='topic'
    )
    job_types = db.relationship(
        'JobType',
        secondary=user_job_type,
        backref='job_type'
    )
    companies = db.relationship(
            'Company',
            secondary=user_company,
            backref='company'
    )

    def __init__(self, user_name, email, password, is_admin=False):
        self.user_name = user_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.is_admin = is_admin
