#!/usr/bin/python3
""" """
from models.base_model import BaseModel, Base
from models.city import City
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv

class test_state(test_basemodel):
    """ """
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=cls.engine)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        Base.metadata.drop_all(bind=cls.engine)

    def test_state_creation(self):
        state = State(name='TestState')
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertEqual(state.name, 'TestState')

    def test_state_relationship_with_city(self):
        if 'db' == getenv("HBNB_TYPE_STORAGE"):
            city = City(name='TestCity')
            state = State(name='TestState', cities=[city])
            self.session.add_all([city, state])
            self.session.commit()
            self.assertIsInstance(state.cities, list)
            self.assertEqual(len(state.cities), 1)
            self.assertEqual(state.cities[0], city)
            self.assertEqual(city.state, state)

    def test_state_table_name(self):
        self.assertEqual(State.__tablename__, 'states')
