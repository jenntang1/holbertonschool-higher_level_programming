#!/usr/bin/python3
""" 13. Delete states """


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    class_session = sessionmaker(bind=engine)

    session = class_session()

    result = session.query(State).filter(State.name.like('%a%')).delete(
        synchronize_session='fetch')

    session.flush()

    session.commit()

    session.close()
