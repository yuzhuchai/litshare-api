import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

loan = Blueprint('loan', 'loan', url_prefix='/loan')

@loan.route('/', methods=['get'])
def check_connection():
	return 'loan blueprint connected'