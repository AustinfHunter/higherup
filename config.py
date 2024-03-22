from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


def get_env_or_throw(key):
    env_var = ""
    try:
        env_var = environ.get(key)
    except KeyError:
        print(f"MISSING ENVIRONMENT VARIABLE: {key}")
        quit(1)
    return env_var


class Config:
    FLASK_DEBUG = get_env_or_throw("FLASK_DEBUG")
    FLASK_ENV = get_env_or_throw("FLASK_ENV")
    SECRET_KEY = get_env_or_throw("SECRET_KEY")

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("DB_URI") or\
        'sqlite:///' + path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS =\
        environ.get("SQL_ALCHEMY_TRACK_MODIFICATIONS") or\
        False
