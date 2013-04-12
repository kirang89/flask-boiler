#!/usr/bin/env bash

pip install virtualenv

#Creating a virtual environment named flask
virtualenv flask

flask/bin/pip install flask
flask/bin/pip install flask-login
flask/bin/pip install flask-openid
flask/bin/pip install flask-mail
flask/bin/pip install flask-sqlalchemy
flask/bin/pip install sqlalchemy-migrate
flask/bin/pip install flask-whooshalchemy
flask/bin/pip install flask-wtf
flask/bin/pip install flask-babel
flask/bin/pip install flup
flask/bin/pip install sqlalchemy==0.7.9
