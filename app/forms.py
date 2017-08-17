from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, PasswordField, BooleanField, validators


class LoginForm(Form):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    remember_me = BooleanField('Remember', default=False)


class RegisterForm(Form):
    username = StringField('Username', validators=[validators.DataRequired()])
    email = StringField('Email', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    password_confirm = PasswordField('Confirm password', validators=[validators.EqualTo('password', message="Passwords do not match")])


class PostForm(Form):
    title = StringField('Title', validators=[validators.DataRequired()])
    content = TextAreaField('Content', validators=[validators.DataRequired()])