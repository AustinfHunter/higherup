from app import db
from app.models.topic import Topic
from app.models.jobtype import JobType
from app.models.skill import Skill
from app.models.company import Company
from app.models.post import Post, PostLike, Comment
from app.posts import bp
from app.posts.forms import PostForm, CommentForm


from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user

import sys


@bp.route('/')
def index():
    posts = Post.get_popular_posts()
    companies = Company.query.all()
    if current_user.is_authenticated:
        return render_template(
            'posts.html',
            user=current_user,
            user_likes=current_user.get_likes(),
            posts=posts,
            companies=companies
        )
    return render_template(
        'posts.html',
        user=current_user,
        posts=posts,
        companies=companies
    )


@bp.route('/<int:post_id>')
def post(post_id):
    form = CommentForm()
    post = Post.query.filter_by(id=post_id).first()
    comments = post.comments.all()
    return render_template(
        'post.html',
        post=post,
        comments=comments,
        form=form,
        user=current_user,
        user_likes=current_user.get_likes()
    )


@bp.route('/add-comment/<int:post_id>', methods=["POST"])
@login_required
def add_comment(post_id):
    form = CommentForm()

    if form.validate_on_submit():
        print("adding comment", file=sys.stdout)
        comment = Comment(post_id, current_user.id, form.content.data)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('posts.post', post_id=post_id))


@bp.route("/createpost", methods=["GET", "POST"])
@login_required
def createpost():
    form = PostForm()
    form.topics.query = Topic.query.all()
    form.skills.query = Skill.query.all()
    form.job_types.query = JobType.query.all()
    form.companies.query = Company.query.all()

    if form.validate_on_submit():
        post = Post(form.title.data, form.content.data, current_user.id)
        post.topics = form.topics.data
        post.companies = form.companies.data
        post.skills = form.skills.data
        post.job_types = form.job_types.data

        db.session.add(post)
        db.session.commit()
        redirect(url_for('posts.post', post_id=post.id))

    return render_template("postEditor.html", form=form, user=current_user)


@bp.route("/deletepost/<int:id>", methods=["DELETE"])
@login_required
def deletepost(id):
    post = Post.query.filter_by(id=id).first()
    if post.author_id == current_user.id:
        db.session.delete(post)
        db.session.commit()
        return {"postUpdate": "deleted"}
    return {"postUpdate": "unchanged"}


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
