from app import db

from app.models.user import User
from app.models.jobtype import JobType
from app.models.skill import Skill
from app.models.topic import Topic
from app.models.company import Company

from sqlalchemy import func

post_topic = db.Table(
    'post_topic',
    db.Column('post_id',
              db.Integer,
              db.ForeignKey('post.id')
              ),
    db.Column('topic_id',
              db.Integer,
              db.ForeignKey('topic.id')
              )
)


post_skill = db.Table(
    'post_skill',
    db.Column('post_id',
              db.Integer,
              db.ForeignKey('post.id')
              ),
    db.Column('skill_id',
              db.Integer,
              db.ForeignKey('skill.id')
              )
)

post_company = db.Table(
    'post_company',
    db.Column('post_id',
              db.Integer,
              db.ForeignKey('post.id')
              ),
    db.Column('company_id',
              db.Integer,
              db.ForeignKey('company.id')
              )
)

post_job_type = db.Table(
    'post_job_type',
    db.Column('post_id',
              db.Integer,
              db.ForeignKey('post.id')
              ),
    db.Column('job_type_id',
              db.Integer,
              db.ForeignKey('job_type.id')
              )
)


class PostLike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    content = db.Column(db.String(2500), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    companies = db.relationship(
        'Company',
        secondary=post_company,
        backref='post_company'
    )
    topics = db.relationship(
        'Topic',
        secondary=post_topic,
        backref='post_topic'
    )
    skills = db.relationship(
        'Skill',
        secondary=post_skill,
        backref='post_skill'
    )
    job_types = db.relationship(
        'JobType',
        secondary=post_job_type,
        backref='post_job_type'
    )
    likes = db.relationship(
        'User',
        secondary='post_like',
        backref='post_likes',
        lazy='dynamic',
    )

    def __init__(self, title, content, author_id):
        self.title = title
        self.content = content
        self.author_id = author_id

    def get_author(self):
        return User.query.filter_by(id=self.author_id).first()

    def get_popular_posts():
        return Post.query.outerjoin(PostLike)\
            .group_by(Post.id)\
            .order_by(func.count(Post.id == PostLike.post_id).desc())\
            .all()
