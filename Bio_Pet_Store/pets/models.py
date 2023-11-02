from pets import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=True, nullable=False)
    last_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')

    def __repr__(self):
        return f"User('{self .first_nameirst_name}, {self.last_nameast_name}, {self.image_file}')"
    
class Pet(db.Model):
    id = db.Column(db.Integer, prmary_key=True)
    name = db.Column(db.String(50), nullable=False, unquote=True)
    price = db.Column(db.Float)

