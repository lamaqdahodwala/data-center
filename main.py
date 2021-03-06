from flask import Flask
import string
import random
import flask_cors
import json
from threading import Thread
from time import sleep
from replit import db as database
app = Flask(__name__)

db = {'aaaaa': 'bbbbb'}


def writetodb():
    while True:
        database = db
        sleep(1)
        
            

Thread(target=writetodb).start()

@app.route('/')
def home():
    return ''

@app.route('/grabdata/<token>')
def grabdata(token):
    pass

@app.route('/updateitem/<item>/<token>/<amount>')
def updatedata(item, token, amount):
    pass

app.run('0.0.0.0')