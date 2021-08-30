"""
Routes and views for the flask application.
"""
import functools
from datetime import datetime
from flask import Flask, request, Response, abort, render_template, flash
from flask_login import current_user,login_user, login_required
from FlaskToDoList import app

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
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username='testuser').first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        login_user(user,form,remember_me.data)
        return redirect(url_for('index'))
 

        if not is_safe_url(next):
            return flask.abort(400)

    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year
        )
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

