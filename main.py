from flask import Flask
import string
import random
import flask_cors
import json
from threading import Thread
from time import sleep
from replit import db
app = Flask(__name__)

flask_cors.CORS(app)


@app.route('/')
def home():
    return ''


@app.route('/exists/<token>')
def exists(token):
    if token in db.keys():
        return 'true'
    else:
        return 'false'


@app.route('/grabdata/<token>')
def grabdata(token):
    pass

@app.route('/updateitem/<item>/<token>/<amount>')
def updatedata(item, token, amount):
    pass

app.run('127.0.0.1', port='8080')