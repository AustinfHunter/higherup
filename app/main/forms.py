from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from app.models.user import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(),
        Length(min=6, max=150)
    ])

    email = EmailField("Email", validators=[
        DataRequired(),
        Email(message=None),
        Length(min=3, max=320)
    ])

    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(min=8, max=25)
    ])

    confirm_password = PasswordField("Repeat password", validators=[
        DataRequired(),
        EqualTo("password", message="Passwords must match.")
    ])

    def validate(self, extra_validators=None):
        init_validtation = super(RegistrationForm, self).validate(extra_validators)
        if not init_validtation:
            return False
        email_exists = User.query.filter_by(email=self.email.data).first()
        name_exists = User.query.filter_by(user_name=self.email.data).first()
        if email_exists:
            self.email.errors.append("Email already in use")
            return False
        if name_exists:
            self.username.erorrs.append("Username already in use")
            return False
        if self.password.data != self.confirm_password.data:
            self.password.errors.append("Passwords must match")
            return False
        return True


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
