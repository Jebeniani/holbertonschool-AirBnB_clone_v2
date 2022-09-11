#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def Cities(self):
            """returns the list of City instances"""
            city_is_red = []
            city_dict = models.storage.all(models.city.City)
            for key, val in city_dict.items():
                if val.state_id == self.id:
                    city_is_red.append(val)
            return city_is_red
    else:
        cities = relationship("City", backref="state",
                            cascade="all, delete-orphan")
