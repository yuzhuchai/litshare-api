from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager
import models

#import blueprint here

DEBUG = True
PORT = 8000

login_manager = LoginManager()

app = Flask(__name__, static_url_path="")
# secret_key
login_manager.init_app(app)

@login_manager.user_loader
# load user method

# set up CORS
# set up blueprint

# before_request decorator

# after_request decorator

@app.route('/')
def index():
	return 'connected'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)