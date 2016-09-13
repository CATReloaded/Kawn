from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from app import App
from app.forms.user_forms import LoginForm
from app.models.accounts import User


@App.route('/')
def index():
    return "Hello"

@App.route('/register', methods=('GET', 'POST'))
def register():
    form = LoginForm()
    if request.method == 'POST':
        # could fail to register user and will not show it
        User.register(form.email.data, form.password.data)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@App.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        user = User.authenticat(form.email.data, form.password.data)
        print user
        if user:
            return redirect(url_for('index'))
        flash("wrong password or email")

    return render_template('login.html', form=form)

@App.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
