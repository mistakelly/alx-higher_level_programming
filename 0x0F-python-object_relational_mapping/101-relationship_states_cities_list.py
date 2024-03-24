#!/usr/bin/python3
"""
All states via SQLAlchemy
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    all_state = session.query(State).all()

    for k in all_state:
        print(f"{k.id}: {k.name}")
        city = k.cities
        for v in city:
            print(f"\t{v.id}: {v.name}")
