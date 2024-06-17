from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[DataRequired(message='Username is required')]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(message='Password is required'), Length(min=6, max=20)]
    )
    remember_me = BooleanField(
        'Remember Me',
    )
    submit = SubmitField(
        'Login'
    )