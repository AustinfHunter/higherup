from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


def get_env_or_throw(key):
    env_var = ""
    try:
        env_var = environ.get(key)
    except KeyError:
        raise Exception(f"MISSING ENVIRONMENT VARIABLE: {key}")
    return env_var


class Config:
    FLASK_DEBUG = get_env_or_throw("FLASK_DEBUG")
    SECRET_KEY = get_env_or_throw("SECRET_KEY")

    # Database
    SQL_ALCHEMY_DB_URI = get_env_or_throw("DB_URI")\
        or 'sqlite:///' + path.join(basedir, 'app.db')
    SQL_ALCHEMY_TRACK_MODIFICATIONS =\
        get_env_or_throw("SQL_ALCHEMY_TRACK_MODIFICATIONS")
