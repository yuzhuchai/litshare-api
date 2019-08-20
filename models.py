from peewee import * #star everything

from flask_login import UserMixin # special mini class that we can inherit from that gives us special properties to help create sessions. 

import datetime # a python module to help deal with dates 


# change this connection when depoly to a real database this is just the file on the computer
DATABASE = SqliteDatabase('litshare.sqlite')



class User(UserMixin, Model):
	username = CharField()
	email = CharField()
	password = CharField()
	bio = TextField()
	zipcode = CharField()

	class Meta:
		database = DATABASE 


class Book(Model):
	title = CharField()
	author = CharField()
	Summary = TextField()
	URL = CharField()
	ISBN = CharField()

	class Meta:
		database = DATABASE 


class Copy(Model):
	owner_id = CharField()
	book_id = CharField()
	condition = CharField()
	Edition = CharField()
	price = CharField()
	rental_time = CharField()
	availbility = CharField()

	class Meta:
		database = DATABASE 


class Request(Model):
	copy_id = CharField()
	owner_id = CharField()
	borrower_id = CharField()
	borrower_notified = CharField()

	class Meta:
		database = DATABASE 


class Loan(Model):
	request_id = CharField()
	date_borrowed = DateTimeField(default=datetime.datetime.now)
	date_due = DateTimeField()
	return_date = DateTimeField(default=none)

	class Meta:
		database = DATABASE 


#create the tables 
def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User,Book,Copy,Request,Loan], safe=True)

	print('table created')
	DATABASE.close()






