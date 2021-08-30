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


login = LoginManager()
login.init_app(app)
app.config['SECRET_KEY'] = 'secret_key'

class User(UserMixin):
    def __init__(self,user_id):
        self.id = user_id

class LoginForm(FlaskForm):
    username = StringField('username')
    password = StringField('password')

@login.user_loader
def load_user(user_id):
    return User(user_id)


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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm() #なんかでるwhy??????????
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.password.data).one_or_none()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        login_user(user,form,remember_me.data)
        return redirect(url_for('index'))

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

