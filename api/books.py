import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

books = Blueprint('books', 'books', url_prefix='/books')

@books.route('/', methods=['get'])
def check_connection():
	return 'books blueprint connected'