# allows Decimals to be used for the objects and database
# SQL Alchemy is ORM 
from sqlalchemy import DECIMAL
from flask_sqlalchemy import SQLAlchemy

# Initializes db
db = SQLAlchemy()

# Database Model used to make orders throughout the web app
class Orders(db.Model):
    orderId = db.Column(db.Integer, primary_key=True)
    truckId = db.Column(db.String(80), unique=False, nullable=False)
    truckCo = db.Column(db.String(80), unique=False, nullable=False)
    customer = db.Column(db.String(80), unique=False, nullable=False)
    job = db.Column(db.String(80), unique=False, nullable=False)
    product = db.Column(db.String(80), unique=False, nullable=False)
    gross = db.Column(DECIMAL(7,2), unique=False, nullable=False)
    tare = db.Column(DECIMAL(7,2), unique=False, nullable=False)
    net = db.Column(DECIMAL(7,2), unique=False, nullable=False)
    tons = db.Column(DECIMAL(7,2), unique=False, nullable=False)

    # assigns a new ID number fro the order
    def __repr__(self):
        return '<Order %r>' % self.orderId