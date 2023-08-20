from . import db 
from flask_login import UserMixin
import datetime

class Users(db.Model, UserMixin): 
    def get_id(self):
        return self.email     
    email = db.Column(db.String(100), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(20))
    # insert code here

class Expenses(db.Model):
    expense_id = db.Column(db.Integer, primary_key=True, nullable=False)
    # insert code here

