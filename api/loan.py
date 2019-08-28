import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

loan = Blueprint('loan', 'loan', url_prefix='/loan')

@loan.route('/', methods=['POST'])
def create_loan():
	payload = request.get_json()
	loan = models.Loan.create(**payload)
	loan_dict = model_to_dict(loan)
	return jsonify(data=loan_dict, status={'code': 201, 'message':'success'})

@loan.route('/', methods=['GET'])
def get_loans():
	try:
		loan_dict = [model_to_dict(loan) for loan in models.Loan.select()]
		return jsonify(data = loan_dict, status = {'code': 200, 'message': 'success'})
	except models.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})


@loan.route('/<loan_id>', methods=['put'])
def return_book(id):
	payload = request.get_json()
	query = models.Loan.update(**payload).where(models.Loan.id == loan_id)
	query.execute()
	loan = models.Loan.get_by_id(loan_id)
	loan_dict = model_to_dict(loan)
	return jsonify(data=loan_dict, status={"code": 200, "message": "Successful update"})

@loan.route('/<loan_id>', methods=['GET'])
def get_one_ask(loan_id):
	try:
		loan_one = [model_to_dict(loan) for loan in moodels.Loan.select().where(models.Loan.id == loan_id)]
		return jsonify(data = loan_one, status = {'code': 200, 'message': 'success'})
	except mdoels.DoesNotExist:
		return jsonify(data = {}, status = {'code': 401, 'message': 'no resource found'})