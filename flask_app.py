# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, Response, request, flash, json, make_response, session
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
from config import CONFIG
import requests

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

authomatic = Authomatic(app.config['OAUTH_CREDENTIALS'], app.secret_key, report_errors=False)

##### ROUTES
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        reason = request.form['reason']
        message = request.form['message']
        hook = "https://hooks.slack.com/services/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"
        headers = {'content-type': 'application/json'}
        payload = {"attachments":[
                {
                   "fallback":"new pgoapi-tracker-flask message!",
                   "pretext":"new pgoapi-tracker-flask message!",
                   "color":"#28d7e5",
                   "fields":[
                      {
                         "title":"from - "  + email,
                         "value":"reason - " + reason + "\n\nmessage - " + message,
                         "short": False
                      }
                   ]
                }
             ]
          }
        r = requests.post(hook, data=json.dumps(payload), headers=headers)
        if r.status_code == 200:
          return render_template('index.html', email = email)
        else:
          return render_template('index.html', error = r.reason)
    else:
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    flash('post')
  else:
    return render_template('login.html')

@app.route('/signup')
def underconstruction():
   return render_template('index.html', underconst = 'Currently under construction!')

@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    response = make_response()
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)

    if result:
      if result.user:
        result.user.update()
      return render_template('login.html', result=result)
    return response
