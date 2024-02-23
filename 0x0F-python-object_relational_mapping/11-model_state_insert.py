#!/usr/bin/python3
"""
Write a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state
- from model_state import Base, State
Your script should connect to a MySQL
server running on localhost at port 3306
Print the new states.id after creation
Your code should not be executed when imported
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def print_state_obj(username, password, db):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    add_column = State(name='Louisiana')

    Base.metadata.create_all(engine)
    session = Session()
    session.add(add_column)
    session.commit()

    result = add_column.id

    return result


if __name__ == '__main__':
    state = print_state_obj(argv[1], argv[2], argv[3])
    print(state)
