import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

ask = Blueprint('ask', 'ask', url_prefix='/requests')

@ask.route('/', methods=['POST'])
def create_ask():
	payload = request.get_json()
	ask = models.Ask.create(**payload)
	ask_dict = model_to_dict(ask)
	return jsonify(data=ask_dict, status={'code':201, 'message':'success'})

@ask.route('/', methods=['GET'])
def get_ask():
	try:
		ask_dict = [model_to_dict(ask) for ask in models.Ask.select()]
		return jsonify(data = ask_dict, status = {'code': 200, 'message': 'success'})
	except models.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})

@ask.route('/<askid>', methods=['PUT'])
def notify_borrower(askid):
	payload = request.get_json()
	query = models.Ask.update(**payload).where(models.Ask.id == askid)
	query.execute()
	updated_ask = models.Ask.get_by_id(askid)
	return jsonify(data=updated_ask, status={'code':201, 'message':'success'})

@ask.route('/<ask_id>', methods=['GET'])
def get_one_ask(ask_id):
	try:
		ask_one = [model_to_dict(ask) for ask in moodels.Ask.select().where(models.Ask.id == ask_id)]
		return jsonify(data = ask_one, status = {'code': 200, 'message': 'success'})
	except mdoels.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})

@ask.route('/<user_id>', methods=['GET'])
def get_asks_for_user(user_id):
	try:
		ask_user = [model_to_dict(ask) for ask in models.Ask.select().where(models.Ask.borrower_id == user_id or models.Ask.owner_id == user_id)]
		return jsonify(data = ask_user, status = {'code': 200, 'message': 'success'})
	except models.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})

@ask.route('/sent/<user_id>', methods=['GET'])
def get_ask_borrower(user_id):
	try:
		ask_sent = [model_to_dict(ask) for ask in models.Ask.select().where(models.Ask.borrower_id == user_id)]

		return jsonify(data = ask_sent, status = {'code': 200, 'message': 'success'})
	except models.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})

@ask.route('/received/<user_id>', methods=['GET'])
def get_ask_owner(user_id):
	try:
		ask_received = [model_to_dict(ask) for ask in models.Ask.select().where(models.Ask.owner_id == user_id)]
		return jsonify(data = ask_received, status = {'code': 200, 'message': 'success'})
	except models.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})

