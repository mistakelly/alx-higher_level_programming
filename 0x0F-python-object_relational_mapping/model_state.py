#!/usr/bin/python3
"""
using sqlalchemy to connect and create a state
table in USE hbtn_0e_6_usa;
sqlalchemy helps us to define databases as python objects and work
with them, so we  don't have to write raw sql codes
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    """
    State Class inherits from Base.
    id(int)
    name(string)
    """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)



