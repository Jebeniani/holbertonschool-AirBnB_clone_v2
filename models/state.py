#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = String(Column(128), nullable=False)
        cities = relationship('City', backref="state", cascade="delete")
    else:
        name = ''

        @property
        def Cities(self):
            """returns the list of City instances"""
            city_is_red = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_is_red.append(city)
            return city_list
