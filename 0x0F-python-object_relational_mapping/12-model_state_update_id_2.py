#!/usr/bin/python3
""" 12. Update a state """


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    class_session = sessionmaker(bind=engine)

    session = class_session()

    update = session.query(State).filter(State.id == '2').first()

    update.name = 'New Mexico'

    session.flush()

    session.commit()

    session.close()
