from flask import Blueprint, render_template, request, url_for, redirect
from . import db
from .models import Users, Expenses
from .forms import AddExpense, ModExpense
from flask_login import current_user, login_required
from datetime import date

views = Blueprint('views', __name__)


@views.route('/expenses')
@login_required
def show_expenses():
    user = Users.query.filter_by(email_address=current_user.email_address).first()
    expenses_user = db.session.query(Expenses).join(Users).filter(Users.id==user.id).all()

    if expenses_user==[]: 
        return render_template("expenses.html", name_user=user.name)
    else: 
        query = Expenses.query.filter (Expenses.user_id== user.id).all()
            
        Total_amount = 0
        for data in query: 
            data.amount
            Total_amount +=data.amount
        total_amount = round(Total_amount,2)

        return render_template("expenses.html", expenses=expenses_user, name_user=user.name, total=total_amount) 


@views.route('/add_expense', methods=['GET', 'POST'] )
@login_required
def adding_new_expenses():
    user = Users.query.filter_by(email_address=current_user.email_address).first()

    form = AddExpense(request.form)

    if request.method == 'GET':
        return render_template("add_expense.html", form=form)
    else:
        if form.validate (): 

            new_expense = Expenses (type_expense= request.values.get ("Type"), 
            description_expense = request.values.get ("Description"), 
            date_purchase = request.values.get ("Date"), 
            amount = request.values.get ("Amount"), 
            user_id = user.id) 

            db.session.add(new_expense)
            db.session.commit()
                    
            return redirect(url_for("views.show_expenses", user = user.name))

            
        else: 
            return render_template("add_expense.html", form=form)


@views.route('/mod_expense', methods=['GET', 'POST'] )
@login_required
def modifying_expenses():   
    user = Users.query.filter_by(email_address=current_user.email_address).first()
    expense_id = request.values.get ("id")

    query = db.session.query (Expenses).filter (Expenses.expense_id == expense_id)

    for data in query: 
        type_expense = data.type_expense
        description_expense = data.description_expense
        date_purchase = data.date_purchase
        amount = data.amount

    if request.method == 'GET':
        form = ModExpense (data= {"Type" : type_expense,
                                "Description": description_expense,
                                "Date": date (int(date_purchase[:4]), int(date_purchase[5:7]), int(date_purchase[8:])),
                                "Amount":amount })
        return render_template("mod_expense.html", form=form)
    else:

        form = ModExpense (request.form)

        if request.form.get ("Delete"): 

            query3 = Expenses.query.filter (Expenses.expense_id == expense_id).first() 
            db.session.delete (query3)
            db.session.commit() 
            return redirect(url_for("views.show_expenses", user=user.name))

        if form.validate(): 
        
            if request.form.get ("Save_changes"): 
                query2 = Expenses.query.filter (Expenses.expense_id == expense_id).all()
                for element in query2: 
                    element.type_expense = form.Type.data
                    element.description_expense = form.Description.data 
                    element.date_purchase = form.Date.data
                    element.amount = form.Amount.data 
                db.session.commit() 
            
                return redirect(url_for("views.show_expenses", user=user.name))
        else: 
            return render_template("mod_expense.html", form=form)

       




