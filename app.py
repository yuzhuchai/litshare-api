from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager
import models

from api.users import users
from api.books import books
from api.requests import requests
from api.loans import loan

DEBUG = True
PORT = 8000

login_manager = LoginManager()

app = Flask(__name__, static_url_path="")
app.secret_key = 'RLAKJDRANDOM STRING'
login_manager.init_app(app)

# @login_manager.user_loader
# load user method

CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(users)

CORS(books, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(books)

CORS(requests, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(requests)

CORS(loan, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(loan)

# before_request decorator

# after_request decorator

@app.route('/')
def index():
	return 'connected'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)