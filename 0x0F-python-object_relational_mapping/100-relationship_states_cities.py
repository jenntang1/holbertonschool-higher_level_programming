#!/usr/bin/python3
""" 15. City relationship """


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)

    class_session = sessionmaker(bind=engine)

    session = class_session()

    data.create_all(engine)

    new_state = State(name='California')

    new_state.city = [City(name='San Francisco')]

    session.add(city)

    session.close()
