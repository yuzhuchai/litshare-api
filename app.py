from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager
import models

from api.users import users
from api.book import book
from api.requests import requests
from api.loans import loan

DEBUG = True
PORT = 8000

login_manager = LoginManager()

app = Flask(__name__, static_url_path="")
# secret_key
app.secret_key = 'RLAKJDRANDOM STRING'


login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
	try: 
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
		return None
# load user method


CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(users)

CORS(book, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(book)

CORS(requests, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(requests)

CORS(loan, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(loan)

# before_request decorator
@app.before_request
def before_request():
	g.db = models.DATABASE
	g.db.connect()

# after_request decorator
@app.after_request
def after_request(response):
	g.db.close()
	return response



@app.route('/')
def index():
	return 'connected'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)