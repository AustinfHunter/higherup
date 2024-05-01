from app import db
from app.models.topic import Topic
from app.models.jobtype import JobType
from app.models.skill import Skill
from app.models.company import Company
from app.models.post import Post, PostLike
from app.models.user import User
from app.posts import bp
from app.posts.forms import PostForm


from flask import render_template, redirect, url_for, request, Response
from flask_login import login_required, current_user


@bp.route('/')
def index():
    posts = Post.get_popular_posts()
    if current_user.is_authenticated:
        user_likes = current_user.liked_posts.all()
        return render_template(
            'posts.html',
            user=current_user,
            user_likes=user_likes,
            posts=posts
        )
    return render_template('posts.html', user=current_user, posts=posts)


@bp.route("/createpost", methods=["GET", "POST"])
@login_required
def createpost():
    author = User.query.filter_by(id=current_user.id).first()
    if not author:
        return redirect(url_for("main.login"))
    form = PostForm()
    form.topics.query = Topic.query.all()
    form.skills.query = Skill.query.all()
    form.job_types.query = JobType.query.all()
    form.companies.query = Company.query.all()

    if form.validate_on_submit():
        post = Post(form.title.data, form.content.data, author.id)
        post.topics = form.topics.data
        post.companies = form.companies.data
        post.skills = form.skills.data
        post.job_types = form.job_types.data

        db.session.add(post)
        db.session.commit()
        redirect(url_for("posts/" + post.id))

    return render_template("post.html", form=form, user=current_user)


@bp.route("/like-post", methods=["POST"])
@login_required
def likepost():
    post_id = request.args.get("post_id")
    cur_like = PostLike\
        .query\
        .filter_by(user_id=current_user.id, post_id=post_id)\
        .first()
    if cur_like:
        db.session.delete(cur_like)
        db.session.commit()
        return {"likeUpdate": "removed"}
    else:
        new_like = PostLike(current_user.id, post_id)
        db.session.add(new_like)
        db.session.commit()
        return {"likeUpdate": "added"}
