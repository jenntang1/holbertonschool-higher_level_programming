#!/usr/bin/python3
""" 14. Cities in state """


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ Subclass inheriting from Base """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
