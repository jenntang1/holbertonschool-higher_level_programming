#!/usr/bin/python3
""" 14. Cities in state """


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

    for result in session.query(State, City).join(State).all():
        print("{}: ({}) {}".format(result.State.name,
                                   result.City.id,
                                   result.City.name))

    session.close()
