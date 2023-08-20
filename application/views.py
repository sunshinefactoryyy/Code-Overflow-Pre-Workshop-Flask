from flask import Blueprint, flash, render_template, request, url_for, redirect
from . import db
from .models import Expenses
from .forms import EditExpense
from flask_login import current_user, login_required
from datetime import date

views = Blueprint('views', __name__)

# CREATE
@views.route('/add_expense', methods=['GET', 'POST'])
@login_required
def adding_new_expenses():

    # insert code here

    return render_template("add_expense.html")


# READ
@views.route('/expenses')
@login_required
def show_expenses():

    # insert code here

    return render_template("expenses.html") 


# UPDATE
@views.route('/mod_expense/<int:expense_id>', methods=['GET', 'POST'])
@login_required
def modifying_expenses(expense_id):

    # insert code here
    return render_template("mod_expense.html")


# DELETE
@views.route('/del_expense', methods=['POST'])
@login_required
def deleting_expenses():

    # insert code here

    return redirect(url_for("views.show_expenses"))




