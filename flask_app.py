
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, Response, request
from flask.ext.login import LoginManager, UserMixin, login_required


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
@app.route('/signup')
def underconstruction():
    return render_template('under-construction.html')

@app.route('/contact-submit', methods=['GET'])
def sendmessage():
	name = request.querystring['name']
	email = request.querystring['email']
	message = request.querystring['message']

	return '<ul><li>' + name + '</li><li>' + email + '</li><li>' + message + '</li></ul>'


