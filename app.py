from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager, login_user, current_user

import models

from api.user import user
from api.book import book
from api.ask import ask
from api.loans import loan

DEBUG = True
PORT = 8000

login_manager = LoginManager()

app = Flask(__name__, static_url_path="")

app.secret_key = 'RLAKJDRANDOM STRING'

login_manager.init_app(app)

# load user method
@login_manager.user_loader
def load_user(userid):
	try: 
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
		return None

# CORS
CORS(user, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(user)

CORS(book, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(book)

CORS(ask, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(ask)

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
	print(current_user, 'current_user id in app')
	app.run(debug=DEBUG, port=PORT)