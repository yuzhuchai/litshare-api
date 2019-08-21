import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict


#first arg is the blueprint name, second arg inport name 
book = Blueprint('book', 'book', url_prefix='/api/books')

@book.route('/', methods=['POST'])
def create_book():
	payload = request.get_json()
	print(payload, 'payload')
	book = models.Book.create(**payload)
	book_dict = model_to_dict(book)
	return jsonify(data=book_dict, status={'code':201, 'message':'success'})




@book.route('/', methods=['GET'])
def get_books():
	try:
		# dict the books found list compheriencahdldadk cant spell
		books = [model_to_dict(book) for book in models.Book.select()]
		return jsonify(data = books, status = {'code': 200, 'message': 'success'})
	except models.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})


@book.route('/<id>', mehtods=['GET'])
def get_one_book(id):
	book = models.Book.get_by_id(id)
	return jsonify(data = book, status = {'code':200, 'message':'success'})


