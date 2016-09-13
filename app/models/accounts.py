from peewee import *
from passlib.hash import sha256_crypt
from flask_login import UserMixin

from app.models.core import Base


class User(Base, UserMixin):
    '''
    User model that represnts all user types in the app
    used for authentcation and authorization
    Note: should only contain methods and fields
          related to this functionalties only
    '''
    email = TextField()
    password = TextField()

    @staticmethod
    def register(email, password):
        password = sha256_crypt.encrypt(password)
        try:
            user = User.get(email=email)
            if user:
                # should raise an exception instead
                raise "this user aleardy exists"
        except: # an apropriate exception should be provided here
            user = User.create(email=email, password=password)
            return user

    @staticmethod
    def authenticat(email, password):
        # if user doesn't exist this will fail badly
        # should be inclosed in an try/except
        user = User.get(email=email)
        # werkzeug provides a good way of hashing and unhashing passwords
        password = sha256_crypt.encrypt(password)

        # this will always return False
        # why do you think? @amrshedou
        if user.password == password:
            return True
        else:
            return False
