import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

loan = Blueprint('loan', 'loan', url_prefix='/loan')

@loan.route('/<id>', methods=['put'])
def return_book(id):
	payload = request.get_json()
	query = models.Loan.update(**payload).where(models.Loan.id == id)
	query.execute()
	loan = models.Loan.get_by_id(id)
	loan_dict = model_to_dict(loan)
	return jsonify(data=loan_dict, status={"code": 200, "message": "Successful update"})
