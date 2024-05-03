from flask import Blueprint

bp = Blueprint('companies', __name__)

from app.companies import routes
