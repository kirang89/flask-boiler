#!/usr/bin/env bash

pip install virtualenv

#Creating a virtual environment named flask
virtualenv flask

#Installing Pylibmc dependencies
sudo apt-get install python-dev
sudo apt-get install libmemcached-dev

#Installing pip modules in the virtual sandbox 'flask'
flask/bin/pip install flask
flask/bin/pip install flask-login
flask/bin/pip install flask-mail
flask/bin/pip install sqlalchemy==0.7.9
flask/bin/pip install flask-sqlalchemy
flask/bin/pip install flask-wtf
flask/bin/pip install flup
flask/bin/pip install pylibmc

