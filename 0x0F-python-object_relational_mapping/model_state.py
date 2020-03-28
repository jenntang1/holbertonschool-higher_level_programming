#!/usr/bin/python3
""" 6. First state model """


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """ Subclass inheriting from Base """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
