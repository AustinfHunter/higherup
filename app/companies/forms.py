from flask_wtf import FlaskForm
from wtforms import StringField, FileField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class CompanyForm(FlaskForm):
    name = StringField(
        "Company Name",
        validators=[DataRequired()],
        name="companyName",
    )
    description = TextAreaField(
        "Company Description",
        validators=[DataRequired()],
        name="companyDescription",
    )
    has_relationship_uncc = BooleanField(
        "Has Relationship With UNCC",
        name="hasRelationship",
    )
    uncc_relationship_desc = TextAreaField(
        "Describe Relationship With UNCC",
        name="relationshipDesc",
    )
    image_upload = FileField(
        "Add Company Image",
        validators=[DataRequired()],
        name="imageUpload",
    )
    website_url = StringField(
        "Link to Company Website",
        name="webUrl",
    )
    website_url_caption = StringField(
        "Caption for Link to Company Website",
        name="webUrlCaption",
    )
