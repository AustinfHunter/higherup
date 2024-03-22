from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    # Application initialization and configuration
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Database setup
    db.init_app(app)

    # TODO:
    # Session management setup
    # login_manager = LoginManager()
    # login_manager.init_app(app)

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
