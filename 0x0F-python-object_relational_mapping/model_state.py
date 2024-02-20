from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

# engin

# create connection
Base = declarative_base()


class State(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))
