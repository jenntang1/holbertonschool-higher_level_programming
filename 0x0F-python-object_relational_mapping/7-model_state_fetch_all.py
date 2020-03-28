#!/usr/bin/python3
""" 7. All states via SQLAlchemy """


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    from sqlalchemy.orm import sessionmaker

    class_session = sessionmaker(bind=engine)

    session = class_session()

    from model_state import Base, State

    for result in session.query(State).order_by(State.id).all():
        print("{}: {}".format(result.id, result.name))

    session.close()
