from app import db
from app.models.user import User
from app.models.topic import Topic
from app.models.jobtype import JobType
from app.models.skill import Skill
from app.models.company import Company
from app.users import bp
from app.users.forms import PreferencesForm

from flask import render_template, redirect, url_for
from flask_login import login_required, current_user


@bp.route("/preferences", methods=["GET", "POST"])
@login_required
def preferences():
    user = User.query.filter_by(id=current_user.id).first()
    if not user:
        return redirect(url_for("main.login"))
    form = PreferencesForm(data={
        "topics": user.topics,
        "skills": user.skills,
        "job_types": user.job_types,
        "companies": user.companies
    })
    form.topics.query = Topic.query.all()
    form.skills.query = Skill.query.all()
    form.job_types.query = JobType.query.all()
    form.companies.query = Company.query.all()

    user = User.query.filter_by(id=current_user.id).first()

    if form.validate_on_submit():
        user.topics.clear()
        user.topics.extend(form.topics.data)

        user.skills.clear()
        user.skills.extend(form.skills.data)

        user.job_types.clear()
        user.job_types.extend(form.job_types.data)

        user.companies.clear()
        user.companies.extend(form.companies.data)

        db.session.commit()

    return render_template("preferences.html", user=user, form=form)
