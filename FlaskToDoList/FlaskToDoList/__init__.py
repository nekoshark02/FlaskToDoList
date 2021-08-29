"""
The flask application package.
"""

from flask import Flask
#from sqlalchemy import SQLAlchemy

app=Flask(__name__,template_folder="/FlaskToDoList/templates",static_folder="/FlaksToDoList/static")

import FlaskToDoList.views

#db = SQLAlchemy

