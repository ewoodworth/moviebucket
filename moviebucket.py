import configparser
from flask import Flask
from flask_session import Session
import logging
import os

logging.basicConfig(format='%(name)s %(asctime)s %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# manage secrets/config elements
config = configparser.ConfigParser()
config.read(os.environ.get('NETWORKING_CONFIG_FILE', './config.ini'))

# set up Flask odds and ends
app = Flask(__name__, instance_relative_config=True)
app.secret_key = config.get('FLASK', 'secret_key')
app.config['SECRET_KEY'] = config.get('FLASK', 'secret_key')
SECRET_KEY = config.get('FLASK', 'secret_key')

def create_app():
    # create and configure the app
    app.config['SESSION_TYPE'] = 'filesystem'
    #logging.getLogger("ncclient.transport.ssh").setLevel(logging.WARNING)
    Session(app)
    #login_manager.init_app(app)
    # FUTURE HOME OF LOGIN STUFF
    return app

def create():
    '''
    Create a movie record
    '''
    return

def list():
    '''
    List all movie records
    '''
    return

def update():
    '''
    Update fields on a movie record
    '''
    return

def delete():
    '''
    Delete a movie record
    '''
    return

# It's a route
@app.route("/")
def root():
    return("Welcome to the whole domain!")

@app.route("/moviebucket")
def moviebucket():
    return("Welcome to Moviebucket!")

# TODO Pretty sure this is *not* how to nest everything under a subdomain... look that up
@app.route("/moviebucket/list_movies")
def list_movies():
    """
    List all movies
    If time add a letter of the alphabet flag
    """
    return

@app.route("/moviebucket/list_my_movies")
def list_my_movies():
    """
    List movies scored by logged in user
    """
    return

@app.route("/moviebucket/delete_movie")
def delete_movie(movie_id):
    """
    Delete a movie record if the user is also the record creator
    """
    return

@app.route("/moviebucket/add_movie")
def add_movie():
    """
    Add a movie record
    """
    return

@app.route("/moviebucket/movie_detail")
def movie_detail(movie_id):
    """
    From a movie id, return the move and all it's 
    fields, set up session such that movie can be scored, 
    edited or deleted
    """
    return


# Context conditionals
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    # logging.getLogger("ncclient.transport.ssh").setLevel(logging.WARNING)
    logger.info("App is running from %s" % __name__)
    app = create_app()
    app.debug = True
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True, port=PORT, use_reloader=False)
    logger.info("server.py is being run directly")
else:
    app = create_app()