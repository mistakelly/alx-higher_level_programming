from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base


# create connection
Base = declarative_base()


class State(Base):
    pass
