from flask import render_template
from app import app


@app.route('/index')
def index():
    user = {'name': 'Kiran'}
    return render_template('index.html', user=user)


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404
