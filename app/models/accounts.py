from peewee import *
from flask_login import UserMixin
from werkzeug import security
from app.models.core import Base

class EmailAlreadyUsed(BaseException):
	pass

class UsernameAlreadyUsed(BaseException):
    pass

class User(Base, UserMixin):
    '''
    User model that represnts all user types in the app
    used for authentcation and authorization
    Note: should only contain methods and fields
          related to this functionalties only
    '''
    email = TextField(unique=True)
    username = TextField(primary_key = True)
    password = TextField()

    @staticmethod
    def register(email, username, password):
        password = security.generate_password_hash(password, method='pbkdf2:sha1', salt_length=8)
        try:
            if User.get(email=email) :
                raise EmailAlreadyUsed
        except User.DoesNotExist:
            try :
                if User.get(username=username) :
                    raise UsernameAlreadyUsed
            except User.DoesNotExist :
                pass
            user = User.create(email=email, username=username, password=password)
            return user

    def authenticat_password(self, password):
        return security.check_password_hash(self.password, password)


    def get_id(self):
        return self.username
