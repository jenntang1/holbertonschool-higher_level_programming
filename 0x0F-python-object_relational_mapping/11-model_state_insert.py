#!/usr/bin/python3
""" 11. Add a new state """


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    class_session = sessionmaker(bind=engine)

    session = class_session()

    new = State(name='Louisiana')

    session.add(new)

    session.flush()

    session.commit()

    result = session.query(State).order_by(State.id.desc()).first()

    print("{}".format(result.id))

    session.close()
