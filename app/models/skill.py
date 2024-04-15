from app import db


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(350), nullable=False)
    is_technical = db.Column(db.Boolean(), nullable=False)

    def __init__(self, name, is_technical=False):
        self.name = name
        self.is_technical = is_technical

    def __str__(self):
        return self.name
