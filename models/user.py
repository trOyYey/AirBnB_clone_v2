#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from os import getenv
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'users'
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        places = relationship("Place", backref="user", cascade='all, delete')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
