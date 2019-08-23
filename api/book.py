import models

from flask import Blueprint, request, jsonify
import simplejson as json
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required


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



@book.route('/<book_id>/copy', methods=['POST'])
@login_required 
def create_copy(book_id):
	'''this function creates a book copy'''
	print("CREATE COPY ROUTE HIT")
	print(current_user,"<----current_user id ")

	payload = request.get_json()
	copy = models.Copy.create(**payload, owner_id=current_user.id, book_id=book_id)
	copy_dict = model_to_dict(copy)
	return jsonify(data=copy_dict, status={'code':200, 'message':'success'})


	
@book.route('/<bookid>/copy' , methods=['GET'])
def get_all_copies(bookid):
	'''get all the copies of a book'''
	print([model_to_dict(copy) for copy in models.Copy.select().where(models.Copy.book_id == bookid)],'<=--------hey yo')

	try:
		copies = [model_to_dict(copy) for copy in models.Copy.select().where(models.Copy.book_id == bookid)]
		# copies = models.Copy.select().where(models.Copy.book_id == bookid)
		# return(copies)
		# print(copies[0]['price'])
		return json.dumps({'data': copies, 'status':{'code':200, 'message':'success'}})
	except models.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})



@book.route('/<bookid>/copy/<copyid>', methods = ['GET'])
def get_one_copy(bookid,copyid):
	'''get one single copy'''
	copy = models.Copy.get_by_id(copyid)
	copy_dict = model_to_dict(copy)
	return json.dumps({'data': copy_dict, 'status': {'code':200, 'message':'success'}})


@book.route('<bookid>/copy/<copyid>', methods= ['PUT'])
def update_edit_copy(bookid,copyid):
	'''edit one copy'''
	payload = request.get_json()
	query = models.Copy.update(**payload).where(models.Copy.id == copyid)
	query.execute()
	updated_copy = models.Copy.get_by_id(copyid)
	return json.dumps({'data':model_to_dict(updated_copy), 'status':{'code':200, 'message':'success'}})


@book.route('<bookid>/copy/<copyid>',methods = ['Delete'])
def delete_copy(bookid, copyid):
	'''this method delete a copy'''
	query = models.Copy.delete().where(models.Copy.id == copyid)
	query.execute()
	return jsonify(data='resource sucessfully deleted', status={'code':200, 'message':'success'})



@book.route('/results', methods=['GET'])
def query_string_search():
	''' this is important!!!!!!!!!get the querying string, inside the react app add ?keyword=(user search input)'''
	# return request.query_string 
	keyword = request.args.get('keyword')
	# return keyword
	books_found = [model_to_dict(book) for book in models.Book.select().where(models.Book.author.contains(keyword) | models.Book.title.contains(keyword))]
	return jsonify(data = books_found, status = {'code':200, 'message':'success'})


