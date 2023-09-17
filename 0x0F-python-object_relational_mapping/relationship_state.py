#!/usr/bin/python3
""" defines a State model.
    inherits from SQLAlchemy Base
    and links to the MySQL table states.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ state class

        attributes:
            __tablename__ (str): The name of the MySQL table to store States
            id (sqlalchemy.Integer): The state's id
            name (sqlalchemy.String): The state's name
            cities (sqlalchemy.orm.relationship): The State-City relationship
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
