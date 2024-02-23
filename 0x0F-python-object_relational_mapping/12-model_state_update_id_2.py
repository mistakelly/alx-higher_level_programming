#!/usr/bin/python3
"""
a script that changes the name of a State
object from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server
running on localhost at port 3306
Change the name of the State where id = 2 to New Mexico
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

    Base.metadata.create_all(engine)
    session = Session()
    update_name = session.query(State).filter_by(id=2).first()

    if update_name:
        update_name.name = 'New Mexico'

    # session.add(update_name)
        session.commit()

        session.close()

        return update_name


if __name__ == '__main__':
    state = print_state_obj(argv[1], argv[2], argv[3])
    # print(state)
