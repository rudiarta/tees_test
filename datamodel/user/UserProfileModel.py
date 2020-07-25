from app import db

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(255))
    profile_picture = db.Column(db.Text)

    def __init__(self, name, username, password, profile_picture):
        self.name = name
        self.username = username
        self.password = password
        self.profile_picture = profile_picture