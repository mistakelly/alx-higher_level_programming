from sys import argv
from sqlalchemy import Column, String, Integer, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('mysql+mysqlconnector://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]), echo=True)

print(engine)


class another_states(Base):
    __tablename__ = 'jamaica'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(135))



class Main_stat(Base):
    __tablename__ = 'australia'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(135))










