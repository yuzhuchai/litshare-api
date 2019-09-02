from peewee import * #star everything

import os
from playhouse.db_url import connect 

from flask_login import UserMixin # special mini class that we can inherit from that gives us special properties to help create sessions. 

import datetime # a python module to help deal with dates 

import os


# DATABASE = connect(os.environ.get('DATABASE_URL'))
# change this connection when depoly to a real database this is just the file on the computer

if os.environ.get('HEROKU_ON'):
	DATABASE = connect(os.environ.get('DATABASE_URL'), pragmas={'ForeignKeyFieldn_keys': 1}) 
else:
	DATABASE = SqliteDatabase('litshare.sqlite', pragmas={'foreign_keys': 1})


class User(UserMixin, Model):
	username = CharField()
	email = CharField()
	password = CharField()
	bio = TextField()
	zipcode = IntegerField()

	class Meta:
		database = DATABASE 


class Book(Model):
	title = CharField()
	author = CharField()
	summary = TextField()
	URL = CharField()
	ISBN = CharField(max_length = 13)

	class Meta:
		database = DATABASE 


class Copy(Model):
	owner_id = ForeignKeyField(User, backref='owner')
	book_id = ForeignKeyField(Book, backref='book')
	condition = CharField()
	edition = CharField()
	price = DecimalField(decimal_places=2, constraints=[Check('price > 0')])
	rental_time = IntegerField()
	availability = BooleanField(default=True)

	class Meta:
		database = DATABASE 


class Ask(Model):
	copy_id = ForeignKeyField(Copy, backref='copy')
	owner_id = ForeignKeyField(User, backref='owner')
	borrower_id = ForeignKeyField(User, backref='borrower')
	ask_date = DateTimeField(default=datetime.datetime.now)
	approval_granted = BooleanField(null=True)

	class Meta:
		database = DATABASE 


class Loan(Model):
	ask_id = ForeignKeyField(Ask, backref='ask')
	date_borrowed = CharField()
	date_due = CharField()
	returned = BooleanField(null=True)

	class Meta:
		database = DATABASE 


#create the tables 
def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User,Book,Copy,Ask,Loan], safe=True)
	print('table created')
	DATABASE.close()






