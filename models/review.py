#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from os import getenv

class Review(BaseModel):
    """ Review classto store review information """
    if 'db' == getenv("HBNB_TYPE_STORAGE"):
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
