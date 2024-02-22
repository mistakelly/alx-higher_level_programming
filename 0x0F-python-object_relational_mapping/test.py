from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class Statesss(Base):

    """
    Class with attributes of a state.
    """

    __tablename__ = 'stateeeeeeee'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

#
# class Main_stat(Base):
#     __tablename__ = 'australia'
#     id = Column(Integer, nullable=False, unique=True, primary_key=True)
#     name = Column(String(135))










