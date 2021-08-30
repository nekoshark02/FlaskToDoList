"""
The flask application package.
"""

from flask import Flask
from flask_login import LoginManager,UserMixin
from sqlalchemy import create_engine
app=Flask(__name__)
import FlaskToDoList.views
engine = create_engine( 'sqlite://' )
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)
login = LoginManager()
login_manager.init_app(app)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30),unique=True)
    passowrd = db.Column(db.String(50),unique=True)

db.create_all()
#DBが空の状態(最初の1回)はtestuserを作成する
user = User.query.filter_by(username='testuser').first()
if user is None:
    testuser = User(username='testuser', e_mail='test@test')
    db.session.add(testuser)
    db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
