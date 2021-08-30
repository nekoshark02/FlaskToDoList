"""
The flask application package.
"""

from flask import Flask
from flask_login import LoginManager,UserMixin,login_user, login_required, logout_user, current_user
from sqlalchemy import create_engine, Column, Table, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app=Flask(__name__)

import FlaskToDoList.views

#######################################################################################


#login = LoginManager()
#login.init_app(app)
#app.config['SECRET_KEY'] = 'secret_key'

#class User(UserMixin):
    #def __init__(self,user_id):
        #self.id = user_id

#class LoginForm(FlaskForm):
    #username = StringField('username')
    #password = StringField('password')

#@login.user_loader
#def load_user(user_id):
    #return User(user_id)

# generate_password_hashとcheck_password__hashをimport
from werkzeug.security import generate_password_hash, check_password_hash

# パスワードをハッシュ化
def set_password(self, password):
        self.password_hash = generate_password_hash(password)

# 入力されたパスワードが登録されているパスワードハッシュと一致するかを確認
def check_password(self, password):
        return check_password_hash(self.password_hash, password)

##うえー