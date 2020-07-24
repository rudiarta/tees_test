from app import db

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    username = db.Column(db.String(128))
    password = db.Column(db.String(255))
    profile_picture = db.Column(db.Text)