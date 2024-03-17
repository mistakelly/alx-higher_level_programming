from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:33066/{}"
                           .format(argv[1], argv[2], argv[3]), pool_pre_ping=True, echo=False)
    Base.metadata.create_all(engine)
    # create session
    Session = sessionmaker(bind=engine)

    session = Session()

    all_data = session.query(State.name, City.id, City.name).filter(State.id == City.state_id)

    for state_name, city_id, city_name in all_data:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

