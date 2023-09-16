#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    sql_engine = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(sql_engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state is None:
        print("Nothing")
    else:
        print('{0}: {1}'.format(state.id, state.name))
