from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, widgets
from wtforms_alchemy import QuerySelectMultipleField


class CheckboxQuerySelectMultipleField(QuerySelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class PostForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[validators.input_required()], name="title"
    )
    content = TextAreaField(
        'Post Content',
        validators=[validators.input_required(), validators.Length(150, 3000)],
        name="content"
    )
    topics = CheckboxQuerySelectMultipleField('Topics')
    skills = CheckboxQuerySelectMultipleField('Skills')
    job_types = CheckboxQuerySelectMultipleField('Job Type')
    companies = CheckboxQuerySelectMultipleField('Companies')


class CommentForm(FlaskForm):
    content = TextAreaField(
        'Comment',
        validators=[validators.input_required(), validators.length(50, 1500)],
        name='content'
    )
