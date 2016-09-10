from flask import Flask
from flask_peewee.db import Database
from flask_wtf import Form
from wtforms import StringField 
from wtforms.validators import DataRequired 
from peewee import *
from flask_login import LoginManager

app = Flask(__name__)
from app.config import base
app.config.from_object(base)

login_manager = LoginManager()
login_manager.init_app(app)
db = Database(app)

class LoginForm(Form):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

from app.models.models import User
User.create_table(fail_silently=True)

from app import views
