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

    # Authentication setup
    login_manager.init_app(app)

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/')
    from app.users import bp as user_bp
    app.register_blueprint(user_bp, url_prefix="/users")
    from app.posts import bp as post_bp
    app.register_blueprint(post_bp, url_prefix="/posts")
    from app.companies import bp as company_bp
    app.register_blueprint(company_bp, url_prefix="/companies")
    return app


@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.query.filter(User.id == int(user_id)).first()
