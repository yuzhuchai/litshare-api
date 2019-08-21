import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

loan = Blueprint('loan', 'loan', url_prefix='/loan')

@loan.route('/<id>', methods=['put'])
def return_book(id):
	payload = request.get_json()
	query = models.Loan.update(**payload).where(models.Loan.id == id)
	query.execute()
	return 'book returned'