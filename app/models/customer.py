from flask import current_app
from app import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    registered_at = db.Column(db.DateTime, nullable=True)
    postal_code = db.Column(db.String)
    phone = db.Column(db.String)
    videos = db.relationship('Video', secondary='rental', backref='customer')

    # videos = db.relationship('Video', backref='customers')
   


    
    