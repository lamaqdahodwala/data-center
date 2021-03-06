from flask import Flask
import string
import random
import flask_cors
from replit import db


app = Flask(__name__)

flask_cors.CORS(app)


@app.route('/')
def home():
    return ''


def exists(token):
    if token in db.keys():
        return True
    else:
        return False

@app.route('/generate')
def gen():
    token = ''
    for i in range(50):
        letter = random.choice(list(string.ascii_letters))
        token += letter
    if exists(token):
        gen()
    else:
        db[token] = {'points': 0}
        return token



@app.route('/grabdata/<token>')
def grabdata(token):
    return str(db[token])

@app.route('/updateitem/<item>/<token>/<amount>')
def updatedata(item, token, amount):
    pass

app.run('0.0.0.0', port='8080')