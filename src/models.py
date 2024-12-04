import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    UserID = Column(Integer, primary_key=True)
    Nickname = Column(String(250), nullable=False)
    Address = Column(String(250), nullable=False)
    Password = Column(String(250), nullable=False)
    Subscription_date = Column(Date, nullable=False)
    favorites = relationship('Favorite', backref="users")

class Planet(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    PlanetID = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Population = Column(String(250), nullable=False)
    Terrain = Column(String(250), nullable=False)
    favorites = relationship('Favorite', backref="planets")
    characters = relationship('Character', backref="planets")

class Character(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    CharacterID = Column(Integer, primary_key=True)
    Gender = Column(String(250), nullable=False)
    Name = Column(String(250), nullable=False)
    Hair_color = Column(String(250), nullable=False)
    Eye_color = Column(String(250), nullable=False)
    favorites = relationship('Favorite', backref="characters")
    PlanetID = Column(Integer, ForeignKey("planets.PlanetID"))

class Favorite(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    UserID = Column(Integer, ForeignKey("users.UserID"), nullable=False, primary_key=True)
    CharacterID = Column(Integer, ForeignKey("characters.CharacterID"))
    PlanetID = Column(Integer, ForeignKey("planets.PlanetID"))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
