from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    remember_me = BooleanField('Remember', default=False)


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    email = StringField('Email', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    password_confirm = PasswordField('Confirm password', validators=[validators.EqualTo('password', message="Passwords do not match")])
