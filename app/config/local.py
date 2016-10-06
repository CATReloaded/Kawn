from app.config.base import *


SECRET_KEY = 'super-secret'

DEBUG = True
DATABASE = {
    'name': 'kawn.db',
    'engine': 'SqliteDatabase',
}
