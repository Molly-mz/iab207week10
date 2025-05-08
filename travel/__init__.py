# import flask - from the package import a module
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    print(__name__)  # let us be curious - what is this __name__
    app = Flask(__name__)  # this is the name of the module/package that is calling this app
    
    Bootstrap5(app) # this is used to display forms QUICKLY

    app.secret_key = 'asecret'
    app.debug = True

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traveldb.sqlite'
    db.init_app(app)
    
    # add the Blueprint
    from . import views
    app.register_blueprint(views.mainbp)
    # add destinations blueprint
    from . import destinations
    app.register_blueprint(destinations.destbp)
    # add authentication bluprint
    from .import auth
    app.register_blueprint(auth.authbp)
    
    return app