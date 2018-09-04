from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlougithub?charset=utf8')
Base = declarative_base()

class Repository(Base):
    __tablename__ = 'repositories'

