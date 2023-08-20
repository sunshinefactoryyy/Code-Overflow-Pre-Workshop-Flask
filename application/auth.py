from flask import Blueprint, flash, render_template, request, url_for, redirect
from . import db
from .models import Users
from .forms import SignUp, Login
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/')
def home(): 
    # insert code here
    return render_template("home.html")


@auth.route('/signup', methods=['GET','POST'])
def signup():
    # insert code here

    return render_template("signup.html")


@auth.route('/login', methods=['GET','POST'])
def login():
    # insert code here

    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.home'))