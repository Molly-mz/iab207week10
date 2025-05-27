from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = db.session.scalars(db.select(Destination)).all()    
    return render_template('index.html', destinations=destinations)

@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        destinations = db.session.scalars(db.select(Destination).where(Destination.description.like(query)))
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))

"""@mainbp.route('/login', methods = ['GET', 'POST'])
def login():
    email = request.values.get("email")
    password = request.values.get("pwd")
    print(f"Email: {email}\nPassword: {password}")
    #Store the email in session 
    session['email'] = request.values.get('email')
    return render_template('login.html')"""

"""@mainbp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
    return 'User logged out'"""



