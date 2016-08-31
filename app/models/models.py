from peewee import *
from datetime import datetime

kawn_db = SqliteDatabase("kawn.db")

class base(Model):
	
	date = DataField(default = datetime.now())
	
	class Meta:
		database = kawn_db
		