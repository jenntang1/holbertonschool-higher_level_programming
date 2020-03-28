#!/usr/bin/python3
""" 7. All states via SQLAlchemy """


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    class_session = sessionmaker(bind=engine)

    session = class_session()

    for result in session.query(State).order_by(State.id).all():
        print("{}: {}".format(result.id, result.name))

    session.close()
