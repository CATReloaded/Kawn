from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from app import App
from app.forms.user_forms import LoginForm
from app.models.accounts import User, UserAlreadyExists


@App.route('/index')
def index():
    return "Hello " + current_user.email

@App.route('/register', methods=('GET', 'POST'))
def register():
    form = LoginForm()
    if request.method == 'POST':
        try:
            User.register(form.email.data, form.password.data)
        except UserAlreadyExists :
            flash('User already registered')
            return redirect(url_for('login'))
        flash('Created user succesfully')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@App.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        try:
            user = User.authenticat(form.email.data, form.password.data)
            if user:
                login_user(user)
                return redirect(url_for('index'))
        except User.DoesNotExist:
            pass
        flash("wrong password or email")
    return render_template('login.html', form=form)

@App.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
