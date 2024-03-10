#!/usr/bin/python3
"""
a script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running
on localhost at port 3306
Your code should not be executed when imported
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def del_state_col(username, password, db):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    del_states = session.query(State).filter(State.name.like('%a%'))

    # loop through the list update_names and drop row
    for del_state in del_states:
        session.delete(del_state)

    # session.add(update_name)
    session.commit()
    session.close()


if __name__ == '__main__':
    del_state_col(argv[1], argv[2], argv[3])
