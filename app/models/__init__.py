from flask import flash
from peewee import *
from passlib.hash import sha256_crypt
from flask_login import login_user, UserMixin
from app import db

class User(db.Model, UserMixin):
	email = TextField()
	password = TextField()

	@staticmethod
	def register(email, password):
		password = sha256_crypt.encrypt(password)
		try:
			user = User.get(email=email)
		except :
			User.create(email=email, password=password)
			flash('created user successfully')
			return
		flash('already registered')

	@staticmethod
	def login(email, password):
		user = User.get(email=email)
		password = sha256_crypt.encrypt(password)
		if user.password == password :
			flash('logged in successfully')
			login_user(user)
		else:
			flash('invalid login')

