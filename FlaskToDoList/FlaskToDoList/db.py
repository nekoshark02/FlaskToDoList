from flask import Flask
from sqlalchemy import create_engine, Column, Table, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from FlaskToDoList import app
engine = create_engine( 'sqlite:///:memory:' )
app.config['SECRET_KEY'] = 'secret_key'
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    username = Column(String(30),unique=True)
    passowrd = Column(String(50),unique=True)
