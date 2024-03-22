from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager


def create_app(config_class=Config):
    # Application initialization and configuration
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Database setup
    db = SQLAlchemy(app)

    # Session management setup
    login_manager = LoginManager()
    login_manager.init_app(app)
    return app
