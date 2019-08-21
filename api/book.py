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






