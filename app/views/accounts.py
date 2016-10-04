from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
import peewee
from app import App
from app.forms.user_forms import LoginForm
from app.models.accounts import User, EmailAlreadyUsed, UsernameAlreadyUsed
from werkzeug import security
from app.models.core import db

@App.route('/index')
def index():
    return "Hello " + current_user.username

@App.route('/<username>')
def profile(username):
    try :
        user = User.get(username=username)
    except User.DoesNotExist :
        flash("User doesn't exist")
        return redirect(url_for('register'))
    return render_template('profile_user.html', user=user)    

@App.route("/edit_profile", methods=('GET', 'POST'))
def edit_profile():
    global current_user
    user = User.get(email=current_user.email)
    form = LoginForm(username=user.username, email=user.email)
    if request.method == "POST" :
        if form.username.data != user.username :
            try:
	            db.execute_sql("UPDATE User SET username=? WHERE email=?;", (form.username.data, user.email))
            except peewee.IntegrityError:
                flash("Username already registered")
        if form.email.data != user.email:
            try :
                db.execute_sql("UPDATE User SET email=? WHERE username=?;", ( form.email.data,user.username))
            except peewee.IntegrityError :
                flash("Email already registered")
        if form.password.data != '':
            User.update(password=security.generate_password_hash(form.password.data, method='pbkdf2:sha1', salt_length=8)).where(username==username).execute()
    return render_template("edit_profile.html", form=form)

@App.route('/register', methods=('GET', 'POST'))
def register():
    form = LoginForm()
    if request.method == 'POST':
        try:
            User.register(form.email.data, form.username.data, form.password.data)
        except EmailAlreadyUsed :
            flash('Email already registered')
            return render_template('register.html', form=form)
        except UsernameAlreadyUsed :
            flash('Username already registered')
            return render_template('register.html', form=form)
        flash('Created user succesfully')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@App.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        try:
            user = User.get(email=form.email.data)
        except User.DoesNotExist:
            try :
                user = User.get(username=form.email.data)
            except User.DoesNotExist:
                user = None
        if user:
            check = user.authenticat_password(form.password.data)
            if check:
                login_user(user)
                return redirect(url_for('index'))
        flash("wrong password or email/username")
    return render_template('login.html', form=form)

@App.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
