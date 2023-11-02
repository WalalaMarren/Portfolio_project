from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, length, Email, EqualTo

#create a register form class
class Register(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), length(min = 2, max =50)])
    last_name = StringField('Last Name', validators=[DataRequired(), length(min = 2, max =50)])
    email = StringField('Email',  validators=[DataRequired(), length(min = 6, max =35)])
    password = PasswordField('Password', validators=[DataRequired(), length(max =6)])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('submit')
    cancel = SubmitField('cancel')

#create a login form
class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), length(min = 6, max =35)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('submit')

    