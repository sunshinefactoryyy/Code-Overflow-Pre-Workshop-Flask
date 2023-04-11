from . import db 
from flask_login import UserMixin
import datetime

class Users(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(50))
    expenses = db.relationship('Expenses', backref='users')

class Expenses (db.Model):
    expense_id = db.Column(db.Integer, primary_key=True, nullable=False)
    type_expense = db.Column(db.String(120), nullable=False)
    description_expense = db.Column(db.String(120), nullable=False)
    date_purchase = db.Column(db.String(10), nullable = False) 
    amount = db.Column(db.Float, nullable = False)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'), nullable=False)

