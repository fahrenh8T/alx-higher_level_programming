#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    sql_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                     .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(sql_engine)
    Session = sessionmaker(bind=sql_engine)

    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')):
        print(state.id, state.name, sep=": ")
