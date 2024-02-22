from sys import argv
from orm import Base, Statesss
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqlconnector://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]), echo=True, pool_pre_ping=True)
    Base.metadata.create_all(engine)
