#!/usr/bin/python3
""" script prints all City objects
    from the database `hbtn_0e_14_usa`
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    """ access to the database and get the cities
        from the database.
    """
    dbengine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                             .format(argv[1], argv[2], argv[3]),
                             pool_pre_ping=True)
    Session = sessionmaker(bind=dbengine)
    session = Session()

    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
