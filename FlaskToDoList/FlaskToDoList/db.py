from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory?charset=utf8', echo = True, future = True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

class User(Base):
    __tablename__ = 'user'  # テーブル名を指定
    username = Column(Integer, primary_key=True)
    password = Column(String)

    def __repr__(self):
        return "<User( username = '%s' , password = '%s' )>"%(
            self.username, self.password)
    
Base.metadata.create_all(engine) 