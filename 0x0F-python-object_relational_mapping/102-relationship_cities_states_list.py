#!/usr/bin/python3
""" script that lists all City objects
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    dbengine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                             .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(dbengine)
    Session = sessionmaker(bind=dbengine)
    session = Session()

    for states in session.query(State).order_by(State.id):
        for city_ins in states.cities:
            print(city_ins.id, city_ins.name, sep=": ", end="")
            print(" -> " + states.name)
