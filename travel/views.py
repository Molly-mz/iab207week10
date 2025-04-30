from flask import Blueprint, render_template, request, session
# Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 

mainbp = Blueprint('main', __name__)

'''@mainbp.route('/')
def index():
    if 'email' in session:
        str = f"Welcome to the Travel App, {session['email']}"
    else:
        str = "<h1>Hello World</h>"
    return render_template('index.html')'''

@mainbp.route('/')
def index():
    return render_template('index.html')

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



