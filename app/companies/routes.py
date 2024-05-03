from flask import render_template,  url_for, redirect, abort
from flask_login import current_user, login_required

from app import db
from app.util.uploads import upload_image

from app.models.company import Company
from app.models.post import Post

from app.companies import bp
from app.companies.forms import CompanyForm


@bp.route('/createcompany', methods=['GET', 'POST'])
@login_required
def create_company():
    if not current_user.is_admin:
        redirect(url_for("main.index"))
    form = CompanyForm()
    if form.validate_on_submit():
        company = Company(form.name.data)
        company.description = form.description.data
        company.has_relationship_uncc = form.has_relationship_uncc.data
        if form.has_relationship_uncc.data:
            company.uncc_relationship_desc = form.uncc_relationship_desc.data

        company.image_url = upload_image(form.image_upload.data)
        company.website_url = form.website_url.data
        company.website_url_caption = form.website_url_caption.data
        db.session.add(company)
        db.session.commit()
    return render_template("companyEditor.html", form=form)


@bp.route('/<string:company_name>')
def company(company_name):
    company = Company.query.filter_by(name=company_name).first()
    if not company:
        abort(404)
    posts = Post.query.join(Post.companies)\
        .filter_by(id=company.id).all()
    return render_template(
        "company.html",
        company=company,
        posts=posts,
        user_likes=current_user.get_likes()
    )
