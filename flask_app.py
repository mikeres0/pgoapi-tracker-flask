# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, Response, request
#from flask.ext.login import LoginManager, UserMixin, login_required


app = Flask(__name__)
#login_manager = LoginManager()
#login_manager.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
def sendmessage():
    email = request.form['email']
    flash('Thanks for the message ' + email)
    return render_template('index.html', email=email)

@app.route('/login')
@app.route('/signup')
def underconstruction():
    return render_template('under-construction.html')


