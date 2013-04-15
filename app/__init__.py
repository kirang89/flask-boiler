from flask import Flask
from werkzeug.contrib.cache import MemcachedCache

app = Flask(__name__)
#Setting up Application Configuration
app.config.from_object('config.ProductionConfig')

#Setting up Cache
cache = MemcachedCache(['127.0.0.1:11211'])

#Setting up File Logging
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/app.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('Application Log')

from app import views
