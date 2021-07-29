from moviebucket import app as application
import logging

gunicorn_logger = logging.getLogger('gunicorn.error')

application.logger.handlers = gunicorn_logger.handlers
application.logger.setLevel(gunicorn_logger.level)

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = gunicorn_logger.level)

if __name__ == "__main__":
    application.run()