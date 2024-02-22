#!/usr/bin/python3
"""
script that prints the first State object
from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state
- from model_state import Base, State
Your script should connect to a MySQL server
running on localhost at port 3306
The state you display must be the first in states.id
You are not allowed to fetch all states from the
database before displaying the result
The results must be displayed as they are in
the example below
If the table states is empty, print Nothing
followed by a new line
Your code should not be executed when imported
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def print_first_state(username, password, db):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db))

    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    Session = session()

    state = Session.query(State).order_by(State.id).first()

    result = '1: {}'.format(state.name)

    Session.close()
    return result


if __name__ == '__main__':
    engine = print_first_state(argv[1], argv[2], argv[3])
    print(engine)
