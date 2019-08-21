import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict


#first arg is the blueprint name, second arg inport name 
book = Blueprint('book', 'book', url_prefix='/books')


@book.route('/', methods=['POST'])
def create_book():
	'''this function is to upload book'''
	payload = request.get_json()
	print(payload, 'payload')
	book = models.Book.create(**payload)
	book_dict = model_to_dict(book)
	return jsonify(data=book_dict, status={'code':201, 'message':'success'})




@book.route('/', methods=['GET'])
def get_books():
	'''this function is to get all the books from db'''
	try:
		# dict the books found list compheriencahdldadk cant spell
		books = [model_to_dict(book) for book in models.Book.select()]
		return jsonify(data = books, status = {'code': 200, 'message': 'success'})
	except models.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})


@book.route('/<id>', methods=['GET'])
def get_one_book(id):
	'''this function is to get one book from db'''
	book = models.Book.get_by_id(id)
	return jsonify(data = model_to_dict(book), status = {'code':200, 'message':'success'})



	

