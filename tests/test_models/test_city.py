#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel, Base
from models.state import State
from models.place import Place
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv

class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @classmethod
    def tearDownClass(cls):
        # close and delete
        cls.session.close()
        Base.metadata.drop_all(bind=cls.engine)

    def test_city_table_name(self):
        # Test the table name of the City class
        self.assertEqual(City.__tablename__, 'cities')

    def test_city_creation(self):
        # creating city with params
        city = City(name='Spodycity', state_id='spodyID')
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertEqual(city.name, 'Spodycity')
        self.assertEqual(city.state_id, 'spodyID')

    def test_city_relationship_with_place(self):
        if getenv("HBNB_TYPE_STORAGE") == 'db':
            state = State(name='TestState')
            city = City(name='TestCity', state=state)
            place = Place(name='TestPlace', city=city)
            self.session.add_all([state, city, place])
            self.session.commit()
            self.assertIsInstance(city.places, list)
            self.assertEqual(len(city.places), 1)
            self.assertEqual(city.places[0], place)
            self.assertEqual(place.cities, city)
