from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from github_loader.config import Config, LOG_FILE_PATH
from github_loader.utils.logger_conf import make_logger

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'

LOGGER = make_logger(LOG_FILE_PATH, 'logger')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)

    from github_loader.main.routes import main
    app.register_blueprint(main)
    return app
