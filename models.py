from app import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.String(12))
    orders = db.Column(db.String(500))

    def __repr__(self):
        return f'<Customer {self.name}>'
