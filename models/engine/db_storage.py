#!/usr/bin/python3

from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
import models

mods = {"User": User, "City": City, "State": State, "Amenity": Amenity,
        "Place": Place, "Review": Review}


class DBStorage:
    """Class engine that is responsible for connecting and storing via MySQL"""
    __engine = None
    __session = None

    def __init__(self):
        """ INITIAL Attribute"""
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{USER}:'
                                      f'{PWD}@{HOST}/{DB}',
                                      pool_pre_ping=True)

        if "test" == getenv('HBNB_ENV'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database"""
        ObjDict = {}
        if cls is None:
            for key in mods:
                for val in self.__session.query(mods[key]):
                    ObjDict[val.__class__.__name__ + '.' + val.id] = val
        else:
            cls = cls if type(cls) != str else mods[cls]
            for val in self.__session.query(cls):
                ObjDict[val.__class__.__name__ + '.' + val.id] = val
        return ObjDict

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current
        database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """ session termination """
        self.__session.close()

    def reload(self):
        """
        create all tables in the database and
        create the current database session
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
