from app import db


class JobType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def to_dict(self):
        return {'id': self.id, 'name': self.name}
