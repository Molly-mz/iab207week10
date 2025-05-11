from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

# Create new destination
class DestinationForm(FlaskForm):
  name = StringField('Country', validators=[InputRequired()])
  description = TextAreaField('Description', 
            validators=[InputRequired()])
  image = FileField('Destination Image', validators=[
    FileRequired(message = 'Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png, jpg, JPG, PNG')])
  currency = StringField('Currency', validators=[InputRequired()])
  submit = SubmitField("Create")
    
# User login
class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

# User register
class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    # submit button
    submit = SubmitField("Register")

# User comment
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