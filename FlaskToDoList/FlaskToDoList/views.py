"""
Routes and views for the flask application.
"""
import functools
from datetime import datetime
from flask import Flask, request, Response, abort, render_template, flash
from flask_login import current_user,login_user, login_required, LoginManager, UserMixin
from FlaskToDoList import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy


login = LoginManager()
login.init_app(app)
app.config['SECRET_KEY'] = 'secret'

db_uri = 'sqlite:///login.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)
####################謎エリア##################

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text())
    password = db.Column(db.Text())
    def __init__(self,username,password):
        self.username = username
        self.password = password

db.create_all()

###############################################
class LoginForm(FlaskForm):
    username = StringField('username')
    password = StringField('password')
    submit = SubmitField('login')

@login.user_loader
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

@app.route('/register',methods=['GET','POST'])
def register():
    """register page """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        flash(error)

    return render_template(
        'register.html',
        title='Register',
        year=datetime.now().year
        )

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm() 
    if form.validate_on_submit():
        if form.username.data == 'nabeou' and form.password.data == 'test':
            user = User(form.username.data)
            login_user(user)
            return redirect('/logout')
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
    return redirect(url_for('index'))


