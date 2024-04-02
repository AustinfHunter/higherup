from app.models.user import User
from app.users import bp

from flask import render_template


@bp.route("/")
def all():
    return render_template('users.html', User.query.all())


@bp.route("/<id>")
def one():
    return render_template('user-admin-view.html', User.query.get(id))
