from flask_wtf import FlaskForm # The base class that all forms should inherit from in Flask-WTF
from wtforms.fields import TextAreaField, SubmitField, StringField, EmailField, PasswordField # Different types of input fields for the form.
from wtforms.validators import InputRequired, Length, Email, EqualTo # Validator to enforce rules (e.g field must be filled in)
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

#Represents a form for creating a new destination. This could be used on a webpage where users
#can submit info about a country they want to add to a travelguide
class DestinationForm(FlaskForm): 
    name = StringField('Country', validators=[InputRequired()])
    #adding two validators, one to ensure input is entered and other to check if 
    #the description meets the length requirements 
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Destination Image', validators = [FileRequired(message = 'Image cannot be empty'), FileAllowed(ALLOWED_FILE, message = 'Only supports png, jpg, JPG, PNG')])
    currency = StringField('Currency', validators=[InputRequired()])
    submit = SubmitField('Create')


#Login the user 
class UserLogin(FlaskForm):
    username = StringField('Username', validators=[InputRequired("Enter username")])
    password = PasswordField('Password', validators=[InputRequired("Enter your password")])
    submit = SubmitField('Login')

#Register the user 
class UserRegister(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[Email("Please enter a valid Email")])
    password = PasswordField('Password', validators=[InputRequired(), 
                                                     EqualTo('confirm', message = "Password should match")])
    confirm = PasswordField("Confirm Password")

    submit = SubmitField("Register")


#used to collect a comment
class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')


#MORE COMPLEX --USE THIS FOR THE ASSIGNMENT

"""
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(message="Username is required."),
        Length(min=4, max=20, message="Username must be between 4 and 20 characters."),
        Regexp(r'^\w+$', message="Username must contain only letters, numbers, or underscores.")
    ])

    email = EmailField('Email', validators=[
        InputRequired(message="Email is required."),
        Email(message="Please enter a valid email address.")
    ])

    password = PasswordField('Password', validators=[
        InputRequired(message="Password is required."),
        Length(min=8, message="Password must be at least 8 characters long."),
        Regexp(r'^(?=.*[A-Z])(?=.*\d).+$',
               message="Password must contain at least one uppercase letter and one number."),
        EqualTo('confirm', message="Passwords must match.")
    ])

    confirm = PasswordField('Confirm Password')

    submit = SubmitField('Register')

"""