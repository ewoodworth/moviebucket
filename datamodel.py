from .moviebucket import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'postgresql+psycopg2://{config.get('PRODUCTION_DB', 'username')}:' +
    f'{config.get('PRODUCTION_DB', 'password')}@' +
    f'{config.get('PRODUCTION_DB', 'host')}/' +
    f'{config.get('PRODUCTION_DB', 'db_name')}'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    amount = db.Column(db.Float)

    def __init__(self, first_name: str, last_name: str, amount: float):
        self.first_name = first_name
        self.last_name = last_name
        self.amount = amount

    def __repr__(self):
        return f'{self.first_name} {self.last_name} spent {self.amount}'

class Movie(db.Model):
    """Movies"""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    title =  db.Column(db.String(50))
    # length between 1 and 50 characters]
    format =  db.Column(db.String(10))
    # allowable values “VHS”, “DVD”, “Streaming”
    length = db.Column(db.Integer)
    # between 0 and 500 minutes] 
    release_year =  db.Column(db.String(25))
    # value between 1800 and 2100] 
    average_rating = db.Column(db.Integer)
    # value between 1 and 5]
    record_creator = db.Column(db.Integer, 
                               db.ForeignKey('users.user_id'), 
                               nullable=False)
    def __repr__(self):
        """
        """
        return "<Movie Title=%s Length=%s>" % (self.title, self.length)

class User(db.Model):
    """Users"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    password = db.Column(db.String(25), 
                         nullable=True)
    username = db.Column(db.String(50), 
                         nullable=True)


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


    # Define relationship to addresses
    address = db.relationship("Address",
                              backref=db.backref("userscores", 
                              order_by=uc_id))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<Userscore uc_id=%s user_id=%s task_id=%s address_id=%s rating=%s commitment=%s>" % (self.uc_id, 
                self.user_id , self.chore_id , self.address_id, self.rating, 
                self.commitment)