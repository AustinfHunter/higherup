from flask import render_template, flash, request, url_for, redirect
from flask_login import login_user, logout_user, current_user

from sqlalchemy import func

from app.main.forms import RegistrationForm, LoginForm

from app import db, bcrypt
from app.main import bp
from app.models.user import User
from app.models.post import Post, PostLike

import sys


@bp.route('/')
def index():
    posts = Post.get_popular_posts()
    if current_user.is_authenticated:
        user_likes = current_user.liked_posts.all()
        return render_template(
            'index.html',
            user=current_user,
            user_likes=user_likes,
            posts=posts)
    return render_template('index.html', user=current_user, posts=posts)


@bp.route('/posts')
def posts():
    posts = Post.get_popular_posts()
    print(posts, file=sys.stdout)
    if current_user.is_authenticated:
        user_likes = current_user.liked_posts.all()
        return render_template(
            'search.html',
            user=current_user,
            user_likes=user_likes,
            posts=posts
        )
    return render_template('search.html', user=current_user, posts=posts)


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
        return redirect(url_for("users.preferences"))
    return render_template("register.html", form=form)


@bp.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("you are already logged in.", "info")
        return redirect(url_for("main.index"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
                user.password,
                request.form["password"]):
            login_user(user)
            print("User logged in")
            return redirect(url_for("main.index"))
        else:
            print("user not logged in")
            flash("Invalid email or password.", "danger")
    return render_template("login.html", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    flash("You were successfully logged out", "success")
    return redirect(url_for("main.login"))


@bp.route("/company")
def company():
    return render_template("companySpecific.html", user=current_user)


@bp.route("/test-headless")
def test_headless():
    if current_user.is_authenticated:
        return {"Authenticated": "true"}
    return {"Authenticated": "false"}
