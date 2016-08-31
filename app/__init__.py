from flask import Flask
from flask_peewee.db import Database
from flask_wtf import Form
from wtforms import StringField 
from wtforms.validators import DataRequired 
from peewee import *
from flask_login import LoginManager

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['DATABASE'] = {
    'name': 'example.db',
    'engine': 'peewee.SqliteDatabase',
}

login_manager = LoginManager()
login_manager.init_app(app)
db = Database(app)

class LoginForm(Form):
	email = StringField('email', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])

from app.models import User
User.create_table(fail_silently=True)

from app import views
