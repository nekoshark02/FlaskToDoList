"""
Routes and views for the flask application.
"""
import functools
import os
import sys
from datetime import datetime
from flask import Flask, request, Response, abort, render_template, flash, redirect
from flask_login import current_user,login_user, login_required, LoginManager, UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, ValidationError
from flask_sqlalchemy import SQLAlchemy

from FlaskToDoList import app

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'secret'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text())
    password = db.Column(db.Text())
    def __init__(self,username,password):
        self.username = username
        self.password = password

db.create_all()

class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
    submit = SubmitField('login')


class EntryForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
    submit = SubmitField('register')


    def validate_name_and_password(self, username):
        if User.query.filter_by(username = username.data).one_or_none():
            raise ValidationError('the')

    def validate_password(self, password):
        if User.query.filter_by(password = password.data).one_or_none():
            raise ValidationError('the')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
        
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='What is "Todui"?'
    )

@app.route('/todo')
def todo():
    """My ToDo Page."""
    return render_template(
        'todo.html',
        title='My ToDo Page',
        year=datetime.now().year,
        message='Welcome to My ToDo Page.'
        )
@app.route('/mytodo')
@login_required
def mytodo():
    return render_template(
        'mytodo.html',
        title='MyToDo',
        year=datetime.now().year,
        message='make your ToDoList'
        )
@app.route('/register', methods=['GET','POST'])
def register():
  register = EntryForm()

  if request.method == "POST":

      if register.validate_on_submit():
        newuser = User(username = register.username.data, password = register.password.data)
        db.session.add(newuser)
        db.session.commit()
        return redirect('/login')
      else:
        flash("false")
        return redirect('/register')

  return render_template(
      'register.html',
      title='Register',
      year=datetime.now().year,
      message='thank you for using Todui!',
      register=register
      )

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm() 
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data, password=form.password.data).one_or_none():
            user = User.query.filter_by(username=form.username.data).one_or_none()
            login_user(user)
            return redirect('/mytodo')
        else:
            return 'Missed'

    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        form = form
        )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template(
        'logout.html',
        title='Logout',
        year=datetime.now().year,
        message ='Thank you for using Todui!'
        )



