# model.py
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('mysql+mysqlconnector://root:31006569@localhost:3306/hbtn_0e_0_usa', echo=True)


class AnotherStates(Base):
    __tablename__ = 'jamaica'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(135))


class MainStat(Base):
    __tablename__ = 'australia'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(135))
