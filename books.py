import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

books = Blueprint('books', 'books', url_prefix='/books')

# start routes here