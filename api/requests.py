import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

requests = Blueprint('requests', 'requests', url_prefix='/requests')

@requests.route('/', methods=['get'])
def check_connection():
	return 'requests blueprint connected'