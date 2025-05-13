from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from flask_login import login_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

# create a blueprint
authbp = Blueprint('auth', __name__ )

@authbp.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        user = User.query.filter_by(email = loginForm.email.data).first()
        if user and check_password_hash(user.password, loginForm.password.data):
            login_user(user)
        
            print('Successfully logged in')
            flash('You logged in successfully')
        else:
            flash('Invalid email or password')
        return redirect(url_for('auth.login'))
    return render_template('user.html', form=loginForm,  heading='Login')

@authbp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    exist = User.query.filter_by(email = form.email.data).first()
    if form.validate_on_submit():
        if exist:
            flash('Email already registered')
            return redirect(url_for('auth.register'))
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            user_name = form.user_name.data, 
            email = form.email.data, 
            password = hashed_password, 
        )
        db.session.add(user)
        db.session.commit()
        print('Successfully registered')
    return redirect(url_for('auth.login'))
    return render_template('user.html', form=form)