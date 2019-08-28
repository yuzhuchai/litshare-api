from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager, current_user
import os
import models

from api.user import user
from api.book import book
from api.ask import ask
from api.loan import loan

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

if 'ORIGIN' in os.environ:
	origin = os.environ['ORIGIN']
else:
	origin = 'http://localhost:3000'

CORS(user, origins= [origin], supports_credentials=True)
app.register_blueprint(user)

CORS(book, origins= [origin], supports_credentials=True)
app.register_blueprint(book)

CORS(ask, origins=[origin], supports_credentials=True)
app.register_blueprint(ask)

CORS(loan, origins=[origin], supports_credentials=True)
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


if 'ON_HEROKU' in os.environ:
    print('hitting ')
    models.initialize()

if __name__ == '__main__':
	models.initialize()
	print(current_user, 'current_user id in app --------------------------')
	app.run(debug=DEBUG, port=PORT)