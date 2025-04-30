from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination, Comment
from .forms import DestinationForm, CommentForm

destbp = Blueprint('destination', __name__, url_prefix = '/destinations')


@destbp.route('/<id>')
def show(id):
    destination = get_destination()
    commentform = CommentForm()
    return render_template('destinations/show.html', destination=destination, form=commentform)
#defines a route at create
# it allows both get and post requests
# Get shows the blank form, Post handles the form after it's submitted

@destbp.route('/create', methods = ['GET', 'POST'])
def create(): #This is run when someone visits /create^
    print('Method type: ', request.method) #debugging
    form = DestinationForm() #creates and instance - it will passed into the HTML template so that the user can fill it out 
    if form.validate_on_submit(): #checks if the form has been submitted and if all fields are valid 
        print('Successfully created new travel destination', 'success')
        return redirect(url_for('destination.create'))
    return render_template('destinations/create.html', form = form)

# Handles when a user submits a comment by creating route in destination.py
destbp.route('/<id>/comment', methods = ['GET', 'POST'])
def comment(id):
    commentform = CommentForm()
    if commentform.validate_on_submit():
        print(f"The following comment has been poasted: {commentform.text.data}")
    return redirect(url_for('destination.show', id = id))

def get_destination():
    # creating a description for of Brazil

    b_desc = """ Brazil is considered an advanced emerging economy.
     It has the ninth largest GDP in the world by nominal, and eight by PPP measures.
     It is one of the world\'s major breadbaskets, being the largest producer of coffee for the last 150 years."""
    
    #An image and a location

    img_location = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag'
    destination = Destination('Brazil', b_desc, img_location, 'R$10')

    #example comments
    comment = Comment("Sam", "Love the view of the place and the coffee is just fantastic", '2023-08-12 11:00:00')
    destination.set_comments(comment)

    comment = Comment("Bill", "free food!", '2023-08-12 11:00:00')
    destination.set_comments(comment)

    comment = Comment("Sally", "free face masks!", '2023-08-12 11:00:00')
    destination.set_comments(comment)

    return destination


