#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))


engine = create_engine('mysql+mysqlconnector://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]), echo=True, pool_pre_ping=True)
#     Base.metadata.create_all(engine)



