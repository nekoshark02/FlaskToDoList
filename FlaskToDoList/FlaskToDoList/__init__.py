"""
The flask application package.
"""

from flask import Flask
#from sqlalchemy import SQLAlchemy

app=Flask(__name__)

import FlaskToDoList.views

#db = SQLAlchemy

