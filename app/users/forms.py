from flask_wtf import FlaskForm
from wtforms_alchemy import QuerySelectMultipleField
from wtforms import widgets


class CheckboxQuerySelectMultipleField(QuerySelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class PreferencesForm(FlaskForm):
    topics = CheckboxQuerySelectMultipleField('Topics')
    skills = CheckboxQuerySelectMultipleField('Skills')
    job_types = CheckboxQuerySelectMultipleField('Job Type')
    companies = CheckboxQuerySelectMultipleField('Companies')
