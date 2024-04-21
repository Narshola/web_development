from flask import Flask, redirect, url_for, session
from random import randint
from db_scripts import *
from queries import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "Shadowplay"

@app.route("/")
def index():
    #session['counter'] = 0
    session['question_id']= 0
    session['quiz_id'] = randint(1, 3)
    return '<a href="/test">Тест</a>'

@app.route("/test")
def test():
    result = get_question_after(session['question_id'], session['quiz_id'])
    if result == None or len(result) == 0:
        return redirect(url_for('results'))
    #session['counter'] += 1
    #return str(session['counter'])
    session['question_id'] = result[0]
    return '<h1>' + str(session['quiz_id']) + '<br>' + str(result) + '</h1>'

@app.route("/results")
def results():
    return '<h1>Тест закончился</h1>'

app.run()