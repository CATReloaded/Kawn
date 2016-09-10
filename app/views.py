from flask import render_template, request, redirect, url_for
from app import app, LoginForm
from app.models.models import User
from flask_login import logout_user

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = LoginForm()
    if request.method == 'POST':
        print('hey there')
        User.register(form.email.data, form.password.data)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        User.login(form.email.data, form.password.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
