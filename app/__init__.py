from flask import Flask
from peewee import *
from flask_login import LoginManager

from app.config import local


App = Flask(__name__)
App.config.from_object(local)


login_manager = LoginManager()
login_manager.init_app(App)

from app.models.accounts import User

@login_manager.user_loader
def load_user(user_id):
	try:
	    return User.get(id=user_id)
	except User.DoesNotExist:
		pass

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')

from app.models.core import db
User.create_table(fail_silently=True)
db.register_fields({'primary_key': 'BIGINT AUTOINCREMENT'})

from app.views.accounts import *
