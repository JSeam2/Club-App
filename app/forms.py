from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField, SubmitField
from wtforms import validators


class LoginForm(FlaskForm):
    email = EmailField("Email Address", [validators.DataRequired(),
                                         validators.Email()])
    password = PasswordField("Password", [validators.DataRequired()])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    email = EmailField("Email Address", [validators.DataRequired(),
                                         validators.Email()])
    password = PasswordField("New Password", [validators.DataRequired()])
    confirm = PasswordField("Repeat Password", [validators.DataRequired(),
                                                validators.EqualTo("password")])
    submit = SubmitField("Create Account")
