#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    if 'db' == getenv("HBNB_TYPE_STORAGE"):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade='all, delete')
    else:
        name = ""
        @property
        def cities(self):
            """getter attribute cities that
            returns the list of City instances"""
            CityList = []
            AllCities = models.storage.all(City)
            for key in AllCities:
                if self.id == AllCities[key].state_id:
                    CityList.append(AllCities[key])
            return CityList
