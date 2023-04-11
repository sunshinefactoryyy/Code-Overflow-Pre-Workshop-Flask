from flask import Blueprint, flash, render_template, request, url_for, redirect
from . import db
from .models import Users
from .forms import SignUp, Login
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import exc

auth = Blueprint('auth', __name__)

@auth.route('/')
def home(): 
    print(Users.query.all())
    if current_user.is_active:
        return redirect(url_for("views.show_expenses"))
    
    return render_template("home.html")


@auth.route('/signup', methods=['GET','POST'])
def signup():
    form = SignUp(request.form)

    if request.method == "POST":
        name = request.form.get('Name')
        email = request.form.get('Email_address')
        password = request.form.get('Password')

        try:
            new_user = Users(name=name, email_address=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
        except exc.IntegrityError as e:
            if 'UNIQUE constraint failed' in str(e):
                flash("This email is already in use, please use a different email")
        else:
            flash('Account created!', category='success')
            return redirect(url_for('auth.home')) 

    return render_template("signup.html", form=form)


@auth.route('/login', methods=['GET','POST'])
def login():
    form = Login(request.form)

    if request.method == "POST":
        email = request.form.get('Email_address')
        password = request.form.get('Password')

        user = Users.query.filter_by(email_address=email).first()
        if user:

            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.show_expenses'))
            else:
                flash('Incorrect password, try again', category='error')
        
        else:
            flash('Email does not exist', category='error')

    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.home'))