import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

ask = Blueprint('asks', 'ask', url_prefix='/requests')

@ask.route('/', methods=['POST'])
def create_request():
	payload = request.get_json()
	print(payload, 'payload')
	request = models.Request.create(**payload)
	request_dict = model_to_dict(request)
	return jsonify(data=book_dict, status={'code':201, 'message':'success'})

@ask.route('/', methods=['GET'])
def get_request():
	try:
		requests = [model_to_dict(request) for request in models.Request.select()]
		return jsonify(data = requests, status = {'code': 200, 'message': 'success'})
	except models.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})