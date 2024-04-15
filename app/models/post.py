from app import db

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


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    content = db.Column(db.String(2500), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __init__(self, title, content, author_id, company_id):
        self.title = title
        self.content = content
        self.user_id = author_id
