#!/usr/bin/python3
"""
Write a script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state
- from model_state import Base, State
Your script should connect to a MySQL server
running on localhost at port 3306
Results must be sorted in ascending order by
states.id
The results must be displayed as they are in the
example below
Your code should not be executed when imported
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def contain_a(username, password, db):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    Session = session()

    # Filter states based on the presence of 'a' in the state name
    all_states = Session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id).all()

    return all_states


if __name__ == '__main__':
    states = contain_a(argv[1], argv[2], argv[3])
    for state_a in states:
        print('{}: {}'.format(state_a.id, state_a.name))
