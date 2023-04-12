from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField, FloatField, HiddenField, PasswordField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Optional
from .models import Users
import re

class Login(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(message='Invalid Email')]) 
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class SignUp(FlaskForm):
    name = StringField('First Name', validators=[Optional(), Length(min=2, max=20)]) 
    email = EmailField('Email*', validators=[DataRequired(), Email(message='Invalid Email')]) 
    password = PasswordField('Password*', validators=[DataRequired(), Length(min=8, max=24)])
    confirm_password = PasswordField('Confirm Password*', validators=[DataRequired(), EqualTo(fieldname="password", message="Passwords must match")])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email is already in use, please use a different one.")
    def validate_password(self, password):
        if not re.fullmatch("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+$", password.data):
            raise ValidationError("Password needs to contain at least one letter, number, and special character.")


Type_of_expense =["Personal", "House", "Transport", "Pets", "Miscellaneous"]

class AddExpense(FlaskForm):
    Expense_id = HiddenField("id")
    Type= SelectField('Type of expense', choices=[(typ, typ) for typ in Type_of_expense])
    Description = StringField('Description of the expense.', validators=[DataRequired()])
    Date= DateField('Purchase Date', format='%Y-%m-%d', validators=[DataRequired()])
    Amount = FloatField('Amount (£)', validators=[DataRequired(message="Invalid amount. Please, introduce a positive number")])

    Add = SubmitField('Add new expense')

    def validate_Amount (self, Amount): 
        if Amount.data <= 0: 
            raise ValidationError ("Invalid amount, please introduce a number greater than 0")


class ModExpense(FlaskForm):
    Expense_id = HiddenField("id")
    Type= SelectField('Type of expense', choices=[(typ, typ) for typ in Type_of_expense])
    Description = StringField('Description of the expense.', validators=[DataRequired()])
    Date= DateField('Purchase Date', format='%Y-%m-%d', validators=[DataRequired()])
    Amount = FloatField('Amount (£)', validators=[DataRequired(message="Invalid amount. Please, introduce a positive number")])

    Save_changes = SubmitField('Save Changes')
    Delete = SubmitField('Delete Expense')

    def validate_Amount (self, Amount): 
        if Amount.data <= 0: 
            raise ValidationError ("Invalid amount, please introduce a number greater than 0")
        
