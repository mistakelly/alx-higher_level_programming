#!/usr/bin/python3
"""select city and also select states (sort of join)
    the code should not execute if imported
"""
from sys import argv
from relationship_state import Base
from relationship_city import City
from relationship_state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:33066/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    # create session
    Session = sessionmaker(bind=engine)

    session = Session()

    session.add(State(name='California'))
    session.add(City(name='San Francisco', state_id=1))
    session.commit()
