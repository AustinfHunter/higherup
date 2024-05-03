from app import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(350), unique=True, nullable=False)
    description = db.Column(db.String(3500))
    has_relationship_uncc = db.Column(db.Boolean)
    uncc_relationship_desc = db.Column(db.String(1200))
    image_url = db.Column(db.String(250))
    website_url_caption = db.Column(db.String(350))
    website_url = db.Column(db.String(500))

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def to_dict(self):
        return {'id': self.id, 'name': self.name}
