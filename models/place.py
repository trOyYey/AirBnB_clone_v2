#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
import models

class Place(BaseModel, Base):
    """ A place to stay """

    if 'db' == getenv("HBNB_TYPE_STORAGE"):
        __tablename__ = "places"
        name = Column(String(128), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0)
        number_bathrooms = Column(Integer, default=0)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Integer, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", 
                                backref="place",
                                cascade='all, delete')
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter attribute reviews that returns the list of Review instances"""
            RevList = []
            AllReviews = models.storage.all(Review)
            for key in AllReviews:
                if AllReviews[key] == self.id:
                    RevList.append(all_reviews[key])
            return RevList

        @property
        def amenities(self):
            """getter for list of all amenities"""
            newList = []
            allAmenities = models.storage.all(Amenity)
            for key in allAmenities:
                if allAmenities[key] in self.amenity_ids:
                    newList.append(allAmenities[key])
            return newList

        @amenities.setter
        def amenities(self, value):
            """setter for new amenity"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
