"""
Routes and views for the flask application.
"""
import functools
from datetime import datetime
from flask import Flask, request, Response, abort, render_template, flash

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
    if request.method == 'POST':
       username = request.form['username']
       password = request.form['password']
       error = None
       if user is None:
            error = 'Incorrect username.'
       ##elif not check_password_hash(user['password'], password):
            #error = 'Incorrect password.'
       flash(error)

    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year
        )



