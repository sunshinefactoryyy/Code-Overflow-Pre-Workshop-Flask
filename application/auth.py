from flask import Blueprint, render_template, request, url_for, redirect
from . import db
from .models import Users
from .forms import AddUser
from datetime import date

auth = Blueprint('auth', __name__)

@auth.route('/')
def home(): 
    count_users = Users.query.count()
    if count_users==0: 
        return render_template("home.html")
    else: 
        users = Users.query.all() 
        return render_template("home.html", users=users)

@auth.route('/add_user', methods=['GET', 'POST'])
def adding_new_users():

    form = AddUser (request.form)

    if request.method == 'GET':
        return render_template("add_user.html", form=form)
    else:
        try: 
            new_user = Users (name = request.values.get ("Name"), email_address = request.values.get ("Email_address") )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("auth.home"))

        except Exception as e:
            error= "" 
            print(e)
            if "users.email_address" in str(e): 
                    error = "This email is already in use, please use a different email"
            return render_template('add_user.html', form=form, error_db_insert=error)