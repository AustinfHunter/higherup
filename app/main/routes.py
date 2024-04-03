from flask import render_template
from app.main import bp


@bp.route('/index')
def index():
    return render_template('index.html')
@bp.route('/search')
def search():
    return render_template('search.html')
@bp.route('/account1')
def account():
    return render_template('account.html')
@bp.route('/officalAccount')
def user_account():
    return render_template('userAccount.html')
@bp.route('/login')
def login():
    return render_template('login.html')
