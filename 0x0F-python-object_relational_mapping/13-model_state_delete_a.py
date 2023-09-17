#!/usr/bin/python3
""" deletes State objects on the database.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    sql_engine = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(sql_engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    stateslogs = session.query(State).filter(State.name.contains('a'))
    if stateslogs is not None:
        for state in stateslogs:
            session.delete(state)

    session.commit()
    session.close()
