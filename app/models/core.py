from peewee import *
from datetime import datetime

kawn_db = SqliteDatabase("kawn.db")

class base(Model):
    created_on = DataField(default = datetime.now())
	
    class Meta:
        database = kawn_db
		