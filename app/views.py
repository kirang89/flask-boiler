from flask import render_template, abort
from app import app


@app.route('/index')
def index():
    user = {'name': 'Kiran'}
    print app.config['NAME']
    return render_template('index.html', user=user)


@app.route('/')
def error():
    return abort(404)
