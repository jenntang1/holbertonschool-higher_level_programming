#!/usr/bin/python3
""" 16. List relationship """


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    class_session = sessionmaker(bind=engine)

    session = class_session()

    for state in session.query(State).all():
        print("{}: {}".format(result.State.id, result.State.name))
        for city in states.cities:
            print("{}: {}".format(result.City.id, result.City.name))
    session.close()
