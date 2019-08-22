### Users blueprint ###
import models

import os
import sys
import secrets
from flask import Blueprint, request, jsonify, url_for
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user', url_prefix='/users')

# start user and authentication routes here

@user.route('/register', methods=['post'])
def register():
	'''this method registers the user'''
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

@user.route('/login', methods=['post'])
def login():
	'''this method logs user in'''
	try:
		payload = request.get_json()
		user = models.User.get(models.User.email == payload['email'])
		print(user)
		if check_password_hash(user.password, payload['password']):
			login_user(user)
			return jsonify(data={model_to_dict(user)}, status={"code": 200, "message": "Login successful"})
		elif not check_password_hash(user.password, payload['password']):
			return jsonify(data={}, status={"code": 401, "message": "Error: incorrect email or password"})
	except models.DoesNotExist:
		print('hitting model does not exist')
		return jsonify(data={}, status={"code": 401, "message": "Error: incorrect email or password"})

@user.route('/logout', methods=['get'])
@login_required
def logout():
	'''this method logs user out'''
	logout_user()
	return 'include redirect here'

@user.route('/<id>', methods=['get'])
def show_user_info(id):
	'''this method shows user's info'''
	user_dict = model_to_dict(current_user)
	del user_dict['password']
	print(user_dict)
	print('user dictionary above ^ ')

	return jsonify(data=user_dict, status={"code": 200, "message": "Success"})

@user.route('/<id>/edit', methods=['put'])
def edit_user_info(id):
	'''this method allows user to update their info'''
	payload = request.get_json()
	query = models.User.update(**payload).where(models.User.id == id)
	query.execute()
	user = models.User.get_by_id(id)
	user_dict = model_to_dict(user)
	return jsonify(data=user_dict, status={"code": 200, "message": "Successful update"})

@user.route('/<id>', methods=['delete'])
def delete_user(id):
	query = models.User.delete().where(models.User.id == id)
	query.execute()
	return jsonify(data='User successfully deleted', status={"code": 200, "message": "Success"})
