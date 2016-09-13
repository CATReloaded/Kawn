from flask import Flask
from peewee import *
from flask_login import LoginManager

from app.config import local


App = Flask(__name__)
App.config.from_object(local)


login_manager = LoginManager()
login_manager.init_app(App)

from app.models.accounts import User
User.create_table(fail_silently=True)

from app.views.accounts import *
