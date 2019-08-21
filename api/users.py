### Users blueprint ###
import models

import os
import sys
import secrets
from flask import Blueprint, request, jsonify, url_for, send_file
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

users = Blueprint('users', 'users', url_prefix='/users')

# start user and authentication routes here

@users.route('/register', methods=['post'])
def register():
	print(request)
	pay_file = request.files
	payload = request.form.to_dict()
	dict_file = pay_file.to_dict()
	return 'hitting register route'
