from app import db

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    shirt_size = db.Column(db.Integer)

    def __init__(self, name, email, shirt_size):
        self.name = name
        self.email = email
        self.shirt_size = shirt_size