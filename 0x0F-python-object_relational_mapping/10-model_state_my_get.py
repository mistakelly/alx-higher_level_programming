#!/usr/bin/python3
"""
Write a script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa

Your script should take 4 arguments: mysql username,
mysql password, database name and state name to search (SQL injection free)
You must use the module SQLAlchemy
You must import State and Base from model_state
- from model_state import Base, State
Your script should connect to a MySQL server running
on localhost at port 3306
You can assume you have one record with the
state name to search
Results must display the states.id
If no state has the name you searched for, display Not found
Your code should not be executed when imported
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def print_state_obj(username, password, db, state_name):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    states = session.query(State).filter(State.name == state_name).first()

    if states is None:
        result = 'Not found'
    else:
        result = states.id

    return result


if __name__ == '__main__':
    state = print_state_obj(argv[1], argv[2], argv[3], argv[4])
    print(state)
