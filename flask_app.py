
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
@app.route('/signup')
def underconstruction():
    return render_template('under-construction.html')



