from flask_wtf import FlaskForm

from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired

class Login_Form(Form):
    username = StringField('User', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_func = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class Search_Query(Form):
    search = StringField('search')
    submit = SubmitField('Find')