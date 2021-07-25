from flask import Flask
import logging

logger = logging.getLogger(__name__)

# manage secrets/config elements
config = configparser.ConfigParser()
config.read(os.environ.get('NETWORKING_CONFIG_FILE', './config.ini'))

# set up Flask odds and ends
app = Flask(__name__, instance_relative_config=True)
app.secret_key = config.get('FLASK', 'secret_key')
app.config['SECRET_KEY'] = config.get('FLASK', 'secret_key')
SECRET_KEY = config.get('FLASK', 'secret_key')

# It's a route
@app.route("/")
def root():
    return("Welcome to Moviebucket!")

# Context conditionals
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    logging.basicConfig(format='%(name)s %(asctime)s %(message)s', level=logging.INFO)
    logging.getLogger("ncclient.transport.ssh").setLevel(logging.WARNING)
    app = create_app()
    app.debug = True
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True, port=PORT, use_reloader=False)
    logger.info("server.py is being run directly")
else:
    # initialize logger if this file is being imported.
    # if the file is being run directly (above) logger
    # will be initialized in create_app
    app = create_app()