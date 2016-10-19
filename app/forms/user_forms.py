from flask_wtf import Form
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required,EqualTo,Email

'''class LoginForm(Form):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
'''
class RegisterForm(Form):
    name = StringField('Name : ')
    password = PasswordField('Password')
    confirm_password = PasswordField('Retype your password')
    email = StringField('Email : ')
    submit = SubmitField('Submit')

#EqualTo('password', message= "Password doesn't match")
#,[Email()]
