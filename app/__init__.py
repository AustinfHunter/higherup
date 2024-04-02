from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_login import LoginManager

from config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(config_class=Config):
    # Application initialization and configuration
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Database setup
    db.init_app(app)

    bcrypt = Bcrypt(app)

    # TODO:
    # Session management setup
    login_manager.init_app(app)
    from app.main import auth

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    return app
