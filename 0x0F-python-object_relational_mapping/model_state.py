#!/usr/bin/python3
"""
using sqlalchemy to connect and create a state
table in USE hbtn_0e_6_usa;
sqlalchemy helps us to define databases as python objects and work
with them, so we  don't have to write raw sql codes
"""
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metaData=MetaData)


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))
