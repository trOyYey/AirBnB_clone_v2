#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)
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

    def test_review_creation(self):
        # Test creating a Review instance
        review = Review(text='TestReview')

        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        self.assertEqual(review.text, 'TestReview')

    def test_review_relationship_with_place_and_user(self):
        if 'db' == getenv("HBNB_TYPE_STORAGE"):
            place = Place(name='TestPlace')
            user = User(name='TestUser')
            review = Review(text='TestReview', place=place, user=user)
            self.session.add_all([place, user, review])
            self.session.commit()
            self.assertEqual(review.place, place)
            self.assertEqual(review.user, user)

    def test_review_table_name(self):
        self.assertEqual(Review.__tablename__, 'reviews')
