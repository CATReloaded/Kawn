from app import db
from app import App
from datetime import *



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), unique = True)
    password = db.Column(db.String(32))
    email = db.Column(db.String(32))
    created_on = db.Column(db.DateTime, default = datetime.now())


db.create_all()
