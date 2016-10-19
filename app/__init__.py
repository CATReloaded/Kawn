from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app import config

App = Flask(__name__)
App.config.from_object(config)

db = SQLAlchemy(App)


login_manager = LoginManager()
login_manager.init_app(App)

from app.models.core import *
from app.forms.user_forms import *
from app.views.new_view import *
