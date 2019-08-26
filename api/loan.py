import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

loan = Blueprint('loan', 'loan', url_prefix='/loan')

@loan.route('/', methods=['POST'])
def create_loan():
	payload = request.get_json()
	loan = models.Ask.create(**payload)
	loan_dict = model_to_dict(loan)
	return jsonify(data=loan_dict, status={'code': 201, 'message':'success'})

@loan.route('/', methods=['GET'])
def get_loans():
	try:
		loan_dict = [model_to_dict(loan) for loan in models.Loan.select()]
		return jsonify(data = loan_dict, status = {'code': 200, 'message': 'success'})
	except models.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})


@loan.route('/<id>', methods=['put'])
def return_book(id):
	payload = request.get_json()
	query = models.Loan.update(**payload).where(models.Loan.id == id)
	query.execute()
	loan = models.Loan.get_by_id(id)
	loan_dict = model_to_dict(loan)
	return jsonify(data=loan_dict, status={"code": 200, "message": "Successful update"})

@loan.route('/<ask_id>', methods=['GET'])
def get_one_ask(loan_id):
	try:
		loanaa_one = [model_to_dict(ask) for ask in moodels.Ask.select().where(models.Ask.id == ask_id)]
		return jsonify(data = ask_one, status = {'code': 200, 'message': 'success'})
	except mdoels.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})