"""
The flask application package.
"""

from flask import Flask
from flask_login import LoginManager

app=Flask(__name__)
import FlaskToDoList.views

login = LoginManager(app)
login.login_view='login'


