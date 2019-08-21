### Users blueprint ###
import models

import os
import sys
import secrets
from flask import Blueprint, request, jsonify, url_for
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from playhouse.shortcuts import model_to_dict

users = Blueprint('users', 'users', url_prefix='/users')

# start user and authentication routes here

@users.route('/register', methods=['post'])
def register():
	payload = request.get_json()
	try:
		models.User.get(models.User.email == payload['email'])
		return jsonify(data={}, status={"code": 401, "message": "A user with that email already exists"})
	
	except models.DoesNotExist:
		payload['password'] = generate_password_hash(payload['password'])
		user = models.User.create(**payload)
		login_user(user)
		user_dict = model_to_dict(user)
		del user_dict['password']
		return jsonify(data=user_dict, status={"code": 201, "message": "Success: user created"})

@users.route('/login', methods=['post'])
def login():
	try:
		payload = request.get_json()
		user = models.User.get(models.User.email == payload['email'])
		print(user)
		if check_password_hash(user.password, payload['password']):
			login_user(user)
			return jsonify(data={}, status={"code": 200, "message": "Login successful"})
		elif not check_password_hash(user.password, payload['password']):
			return jsonify(data={}, status={"code": 401, "message": "Error: incorrect email or password"})
	except models.DoesNotExist:
		print('hitting model does not exist')
		return jsonify(data={}, status={"code": 401, "message": "Error: incorrect email or password"})

@users.route('/logout', methods=['get'])
@login_required
def logout():
	logout_user()
	return 'include redirect here'



