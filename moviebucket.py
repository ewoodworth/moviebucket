import configparser
from flask import Flask, request
from flask_session import Session
import logging
import os
import configparser
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from werkzeug.security import generate_password_hash, check_password_hash

# Logging Odds and Ends
logging.basicConfig(format='%(name)s %(asctime)s %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# manage secrets/config elements
config = configparser.ConfigParser()
config.read(os.environ.get('CONFIG_FILE', './config.ini'))


# Flask odds and ends
app = Flask(__name__, instance_relative_config=True)
app.secret_key = config.get('FLASK', 'secret_key')
app.config['SECRET_KEY'] = config.get('FLASK', 'secret_key')
# SECRET_KEY = config.get('FLASK', 'secret_key')

# Flask SQLAlchemy Odds and Ends
db_user = config.get('PRODUCTION_DB', 'username')
db_pass = config.get('PRODUCTION_DB', 'password')
db_host = config.get('PRODUCTION_DB', 'host')
db_name = config.get('PRODUCTION_DB', 'db_name')

app.config['SQLALCHEMY_DATABASE_URI'] = (f'postgresql+psycopg2://{db_user}:\{db_pass}@{db_host}/{db_name}')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#
# SQLAlchemy Classes
#

class Movie(db.Model):
    """Movies"""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    title =  db.Column(db.String(50))
    format =  db.Column(db.String(10))
    length = db.Column(db.Integer)
    release_year =  db.Column(db.String(25))
    average_rating = db.Column(db.Integer)
    record_creator = db.Column(db.Integer, 
                               db.ForeignKey('users.user_id'), 
                               nullable=False)
    def __repr__(self):
        """
        """
        return "<%s: %s from %s as %s, Length:%s min Rated %s/5>" % (str(self.id), 
                                                                          self.title, 
                                                                          str(self.release_year),
                                                                          self.format, 
                                                                          str(self.length),
                                                                          str(self.rating))

class User(db.Model):
    """Users"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    password_hash = db.Column(db.String(128), 
                              nullable=False)
    username = db.Column(db.String(50), 
                         nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



    def __repr__(self):
        """
        """
        return "<User user_id=%s name=%s>" % (self.user_id, self.username)

class Userscore(db.Model):
    """Association table for users and movies"""

    __tablename__ = "userscores"

    uc_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('chores.chore_id'), 
              nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), 
              nullable=False)
    individual_rating = db.Column(db.Integer)


    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<Userscore uc_id=%s user_id=%s task_id=%s address_id=%s rating=%s commitment=%s>" % (self.uc_id, 
                self.user_id , self.chore_id , self.address_id, self.rating, 
                self.commitment)

#
# FLASK Methods
#

def create_app():
    # create and configure the app
    app.config['SESSION_TYPE'] = 'filesystem'
    #logging.getLogger("ncclient.transport.ssh").setLevel(logging.WARNING)
    Session(app)
    #login_manager.init_app(app)
    # FUTURE HOME OF LOGIN STUFF
    return app

# It's a route
@app.route("/")
def root():
    return("Welcome to the whole domain!")

@app.route("/moviebucket")
def moviebucket():
    return("Welcome to Moviebucket!")

@app.route("/list_all_movies", methods=['GET'])
def list_movies():
    """
    List all movies
    If time add a letter of the alphabet flag
    curl -X GET "https://ip-address/list_movies" -H "username:admin" -H "password:foo"
    """
    username = request.headers['username']
    password = request.headers['password']
    # These would get validated through the records in our DB and a user id would wind 
    # up as a session variable of some kind.
    
    movies = Movie.query.all()
    return '\n'.join([str(movie) for movie in moviess])

# This does truly nothing... but it should
# @app.route("/list_my_movies", methods=['GET'])
# def list_my_movies():
#     """
#     List movies scored by logged in user
#     curl -X GET "https://ip-address/list_movies" -H "username:admin" -H "password:foo"
#     """
#     return

@app.route("/moviebucket/delete_movie/<id>", methods=['DELETE'])
def delete_movie(movie_id):
    """
    Delete a movie record if the user is also the record creator
    curl -X DELETE "ip-address/delete_movie" -H "accept: application/json" -H "username:admin" -H "password:foo"
    """
    username = request.headers['username']
    password = request.headers['password']    
    # These would get validated through the records in our DB and a user id would wind 
    # up as a session variable of some kind.
    user_id = session_owner

    movie = Movie.query.filter_by(movie_id=id).first()

    if movie.record_creator == user_id:
        message = str(movie)
        db.session.delete(movie)
        return(message)
    else:
        return("Sorry, records can only be updated by their creator.")

@app.route("/update_movie/<id>", methods=['PUT'])
def update_movie(id):
    """
    Add a movie record
    curl -X PUT "http://192.168.42.6:5000/add_movie" -H "accept: application/json" -H "Content-Type: application/json" -H "username:admin" -H "password:foo" -d "{\"title\": \"THE_TITLE\",\"format\": \"FORMAT_KEY\",\"length\": \"LENGTH\",\"release date\": \"RELEASE_DATE\",\"rating\":\"RATING\"}"
    """
    username = request.headers['username']
    password = request.headers['password']
    # These would get validated through the records in our DB and a user id would wind 
    # up as a session variable of some kind.
    user_id = session_owner

    response = dict(request.get_json())
    movie = Movie.query.filter_by(movie_id=id).first()

    if movie.record_creator = user_id:
        title = response['title']
        format = response['format']
        length = response['length']
        release_date = response['release date']
        rating = response['rating']

        # React forms would have these built in, and these would be secondary vallidations.
        if 0 == len(title) or 50 < len(title):
            return("Please try again with a title between 1 and 50 chars")
        if format.lower() not in {'VHS','DVD','Streaming'}:
            return("Please try again and enter one of 'DVD', 'VHS' or 'Streaming' for format")
        if 0 == length or 500 < length:
            return("Please try again with a length between 0 and 500")
        if 1800 > int(release_date) or 2100 < int(release_date):
            return("Please try again. Release year must be between 1800 and 2100")
        if 1 >= int(rating) or 5 < int(rating):
            return("Please try again with a rating between 1 and 5")

        # SQLAlchemy prevents injection attacks but I'm being a bit extra here:
        movie.title = str(title)
        movie.format = str(format)
        movie.length = int(length)
        movie.release_year = int(release_date)
        db.session.commit()
        return('Updated: %s' % movie)
    else:
        return ("Sorry, records can only be updated by their creator.")

@app.route("/add_movie", methods=['POST'])
def add_movie():
    """
    Add a movie record
    curl -X POST "http://192.168.42.6:5000/add_movie" -H "accept: application/json" -H "Content-Type: application/json" -H "username:admin" -H "password:foo" -d "{\"title\": \"THE_TITLE\",\"format\": \"FORMAT_KEY\",\"length\": \"LENGTH\",\"release date\": \"RELEASE_DATE\",\"rating\":\"RATING\"}"
    """
    username = request.headers['username']
    password = request.headers['password']
    # These would get validated through the records in our DB and a user id would wind 
    # up as a session variable of some kind.
    user_id = session_owner

    response = dict(request.get_json())

    title = response['title']
    format = response['format']
    length = response['length']
    release_date = response['release date']
    rating = response['rating']

    # React forms would have these built in, and these would be secondary vallidations.
    if 0 == len(title) or 50 < len(title):
        return("Please try again with a title between 1 and 50 chars")
    if format.lower() not in {'VHS','DVD','Streaming'}:
        return("Please try again and enter one of 'DVD', 'VHS' or 'Streaming' for format")
    if 0 == length or 500 < length:
        return("Please try again with a length between 0 and 500")
    if 1800 > int(release_date) or 2100 < int(release_date):
        return("Please try again. Release year must be between 1800 and 2100")
    if 1 >= int(rating) or 5 < int(rating):
        return("Please try again with a rating between 1 and 5")

    # SQLAlchemy prevents injection attacks but I'm being a bit extra here:
    movie = Movie(title = str(title),
                  format = str(format),
                  length = int(length),
                  release_year = int(release_date),
                  record_creator = user_id)
    db.session.add(movie)
    db.session.commit()

    userscore = Userscore(movie_id = movie.id, 
                          user_id = user_id, 
                          individual_rating = int(rating))
    db.session.add(userscore)
    db.session.commit()
    return('Added: %s' % movie)

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