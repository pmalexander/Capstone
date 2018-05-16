from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Text, ForeignKey, Time, desc
from flask_login import UserMixin

import psycopg2

from . import app

# engine derived from app.config (config.py info)
# the data is stored in teh varaible SQLALCHEMY_DATABASE_URI
engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

import os, time
import datetime
from datetime import datetime

###need to change to streamlined format (all in one line)
class Location(Base):
    __tablename__ = "location"
    
#ISSUE - REGION IS GENERAL, LAT AND LONG DENOTE SOMETHING SPECIFIC - REMOVED REGION
#BECAUSE THE LAT AND LONGITUDE ARE PRECISE, THEY CAN MEASURE DISTANCE BETWEEN EACH OTHER,
#USE LAT AND LONG, THINK OF THIS AS A MAPPING TOOL IN THAT SENSE
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    region = Column((String)(1024))
    country = Column((String)(1024))
    latitude = Column(Float)
    longitude = Column(Float)
    visitors = Column(Integer)
    overview = Column(String(1024))
    
    def __init__(self, name, region, country, latitude, longitude, visitors, overview):
        self.name = name
        self.region = region
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.visitors = visitors
        self.overview = overview
    
    # one fauna to many locations, since fauna can be found in many locations
    fauna_id = Column(Integer, ForeignKey("fauna.id"))
    # one flora to many locations, ditto to above
    flora_id = Column(Integer, ForeignKey("flora.id"))
    # many landmarks to one location
    features = relationship("Feature", backref="location_features")

# as stated above, fauna is not exclusive to a single location, some places may not have fauna in the same range
class Fauna(Base):
    __tablename__ = "fauna"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    
    def __init__(self, name, characteristics):
        self.name = name
        self.characteristics = characteristics
   
    loc_id = Column(Integer, ForeignKey(Location.id), nullable=True)

# same with flora, flora is not exclusive to a single location, some places may not have flora in the same range
class Flora(Base):
    __tablename__ = "flora"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))

    def __init__(self, name, characteristics):
        self.name = name
        self.characteristics = characteristics
    
    loc_id = Column(Integer, ForeignKey(Location.id), nullable=True)

# certain landmarks are endemic to specific sites, many can exist in one site
class Feature(Base):
    __tablename__ = "feature"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    
    def __init__(self, name, characteristics):
        self.name = name
        self.characteristics = characteristics
    
    loc_id = Column(Integer, ForeignKey(Location.id), nullable=True)
    #assoc_feature = relationship("Location", backref="assoc_feature")
    
    # there are multiple UNIQUE landmarks in one location, so this is many to one
    #location = Column(Integer, ForeignKey("locations.id"))

# establishes user information parameters
class User(Base, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))
    sighting = relationship("Sighting", backref="author")

# creates parameters for inventory items stored in the database
class Inventory(Base):
    __tablename__ = "inventory"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    characteristics = Column((String)(1024))

# creates parameters for adding the sightings by users    
class Sighting(Base):
    __tablename__ = "sightings"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(1024))
    content = Column(Text)
#    datetime = Column(DateTime, default=datetime.datetime.now)
    author_id = Column(Integer, ForeignKey('users.id'))
    
# creates the database, everything following up is what will be loaded into the database
Base.metadata.create_all(engine)