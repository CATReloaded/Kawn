from peewee import *
from datetime import datetime

from app import utils
# FIX should find out automaticly
# which config module to load the DATABASE from
# @bisho
from app.config.local import DATABASE


db = utils.get_db(DATABASE['name'], DATABASE['engine'])


class Base(Model):
    '''
    Serves as the Base model for all app models
    Common functionalties and fields is implemented here
    '''
    created_on = DateField(default=datetime.now())

    class Meta:
        database = db
