from flask import render_template, flash, request, url_for, redirect
from flask_login import login_user, logout_user, current_user

from app.main.forms import RegistrationForm, LoginForm

from app import db, bcrypt
from app.main import bp
from app.models.user import User


@bp.route('/')
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


@bp.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already registered.", "info")
        return redirect(url_for("main.index"))
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash("Registration successfull! You are now logged in", "success")

        return redirect("main.index")
    return render_template("register.html", form=form)


@bp.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("you are already logged in.", "info")
        return redirect(url_for("main.index"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        password_valid = bcrypt.check_password_hash(
            user.password,
            request.form["password"]
        )

        if user and password_valid:
            login_user(user)
            return redirect(url_for("main.index"))
        else:
            flash("Invalid email or password.", "danger")
    return render_template("login.html", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    flash("You were successfully logged out", "success")
    return redirect(url_for("main.login"))
