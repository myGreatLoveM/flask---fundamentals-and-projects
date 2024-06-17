from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Optional, EqualTo

class RegisterForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[DataRequired(message='Username is required'), Length(min=3, max=30)]
    )
    email = StringField(
        label='Email',
        validators=[DataRequired(message='Email is required'), Email()]
    )
    gender = SelectField(
        label='Gender',
        choices=['Male', 'Female', 'Other'],
        validators=[Optional()]
    )
    dob = DateField(
        'Date of Birth',
        validators=[Optional()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(message='Password is required'), Length(min=6, max=20)]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(message='Confirm Password is required'), Length(min=6, max=20), EqualTo(fieldname='password')]
    )
    submit = SubmitField(
        'Register'
    )


class LoginForm(FlaskForm):
    email = StringField(
        label='Email',
        validators=[DataRequired(message='Email is required'), Email()]
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