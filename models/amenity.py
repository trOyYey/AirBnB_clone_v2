o#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from os import getenv
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    '''Class defining '''

    if 'DB' == getenv("HBNB_TYPE_STORAGE"):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                        viewonly=False, 
                                        back_populates="amenities")
    else:
        name = ""
