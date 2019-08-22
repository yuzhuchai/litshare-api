import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

ask = Blueprint('asks', 'ask', url_prefix='/requests')

@ask.route('/', methods=['POST'])
def create_ask():
	payload = request.get_json()
	ask = models.Ask.create(**payload)
	ask_dict = model_to_dict(ask)
	return jsonify(data=ask_dict, status={'code':201, 'message':'success'})

@ask.route('/', methods=['GET'])
def get_ask():
	try:
		ask = [model_to_dict(ask) for ask in models.Ask.select()]
		return jsonify(data = ask, status = {'code': 200, 'message': 'success'})
	except models.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})