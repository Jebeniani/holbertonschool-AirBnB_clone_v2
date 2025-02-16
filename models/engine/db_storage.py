#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """a database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{]".format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True))
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session
        all objects depending of the class name"""
        if cls is None:
            for obj in self.__session.query(User, State, City,
                                            Amenity, Place, Review)
            key = "{}.{}".format(type(obj).__name__, obj.id)
            obdi[key] = obj
        return obdi

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database & the current database session"""
        Base.metadata.create_all(self.__engine)
        Sessio = sessionmaker(binds=self.__engine,
                            expire_on_commit=False)
        Session = scoped_session(sessio)
        self.__session = sessio()
