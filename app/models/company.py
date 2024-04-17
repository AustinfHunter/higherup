from app import db
from app.models.post import Post


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(350), unique=True, nullable=False)
    description = db.Column(db.String(1200))
    useLocalImageUrl = db.Column(db.Boolean)
    localImageUrl = db.Column(db.String(150))
    imageUrl = db.Column(db.String(250))
    posts = db.relationship('Post', backref='company', lazy=True)

    def __init__(self, name):
        self.name = name

    def addInfo(self, description, useLocalImageUrl, localImageUrl, imageUrl):
        self.description = description
        self.useLocalImageUrl = useLocalImageUrl
        self.localImageUrl = localImageUrl
        self.imageUrl = imageUrl

    def __str__(self):
        return self.name
