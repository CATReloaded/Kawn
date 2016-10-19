from app import App
from app.forms.user_forms import *
from flask import render_template
from app import db
from app.models.core import *


@App.route('/')
def index():
    return 'Hello World !!'

@App.route('/register', methods = ['GET', 'POST'])
def register():
    print 'Hau'
    form = RegisterForm()
    if form.validate_on_submit():
        print 'bb'
        if user.query.filter_by(name = form.name.data).first():
            print 'This email or name already exists'
        else:
            print 'Good'
            new_user = User(name = form.name.data, email = form.email.data, password = form.password.data)
            db.session.add(new_user)
            db.session.commit()
    return render_template('register.html', form = form)
