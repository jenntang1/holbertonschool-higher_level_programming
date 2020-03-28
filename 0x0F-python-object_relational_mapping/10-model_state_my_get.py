#!/usr/bin/python3
""" 10. Get a state """


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    class_session = sessionmaker(bind=engine)

    session = class_session()

    result = session.query(State).filter(State.name == argv[4])

    all_result = result.all()

    if not all_result:
        print("Not found")
    else:
        for sub_result in result:
            print("{}".format(sub_result.id))

    session.close()
