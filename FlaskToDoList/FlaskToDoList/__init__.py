"""
The flask application package.
"""

from flask import Flask
from flask_login import LoginManager,UserMixin,login_user, login_required, logout_user, current_user
from sqlalchemy import create_engine, Column, Table, Integer, String
from sqlalchemy.ext.declarative import declarative_base
app=Flask(__name__)
import FlaskToDoList.views
engine = create_engine( 'sqlite:///:memory:' )
app.config['SECRET_KEY'] = 'secret_key'
Base = declarative_base()
login = LoginManager(app)
login.login_view='login'
#login_manager.login_message="Oops! Please try logging in"

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    username = Column(String(30),unique=True)
    passowrd = Column(String(50),unique=True)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(id))
