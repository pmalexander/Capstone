from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Text, ForeignKey, Time, desc
from flask_login import UserMixin
from flask import Base

import psycopg2

from . import app

# engine derived from app.config (config.py info)
# the data is stored in teh varaible SQLALCHEMY_DATABASE_URI
engine = create_engine(app.config["Config.SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

import os, time
import datetime
from datetime import datetime

###need to change to streamlined format (all in one line)
class Location(Base):
    __tablename__ = "locations"

#ISSUE - REGION IS GENERAL, LAT AND LONG DENOTE SOMETHING SPECIFIC - REMOVED REGION
#BECAUSE THE LAT AND LONGITUDE ARE PRECISE, THEY CAN MEASURE DISTANCE BETWEEN EACH OTHER,
#USE LAT AND LONG, THINK OF THIS AS A MAPPING TOOL IN THAT SENSE
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    latitude = Column(Float)
    longitude = Column(Float)
    visitors = Column(Integer)
    
    # one fauna to many locations, since fauna can be found in many locations
    fauna_id = Column(Integer, ForeignKey("Fauna.id"))
    # one flora to many locations, ditto to above
    flora_id = Column(Integer, ForeignKey("Flora.id"))
    # many landmarks to one location
    features = relationship("Feature", backref="location_features")

# as stated above, fauna is not exclusive to a single location, some places may not have fauna in the same range
class Fauna(Base):
    __tablename__ = "fauna"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    location_fauna = relationship("Location", backref="locations")
    assoc_fauna = relationship("Location", backref="assoc_fauna")
    loc_id = Column(Integer, ForeignKey(Location.id, nullable=False))

# same with flora, flora is not exclusive to a single location, some places may not have flora in the same range
class Flora(Base):
    __tablename__ = "flora"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    assoc_flora = relationship("Location", backref="assoc_flora")
    loc_id = Column(Integer, ForeignKey(Location.id, nullable=False))

# certain landmarks are endemic to specific sites, many can exist in one site
class Feature(Base):
    __tablename__ = "features"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    loc_id = Column(Integer, ForeignKey(Location.id, nullable=False))
    assoc_feature = relationship("Location", backref="assoc_feature")
    
    # there are multiple UNIQUE landmarks in one location, so this is many to one
    location = Column(Integer, ForeignKey("locations.id"))

# establishes user information parameters
class User(Base, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))

# creates parameters for inventory items stored in the database
class Inventory(Base):
    __tablename__ = "inventory"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    characteristics = Column((String)(1024))

# creates the database, everything following up is what will be loaded into the database
Base.metadata.create_all(engine)

# need to change to streamlined format (all in one line)

################################
###PARKS/RESERVES/WHATHAVEYOU###
################################

#all visitor numbers are placeholders, will probably leave out in later version
# adds national park/reserves to be queried in database, latitude and longitude of location saved
# region (general) was removed due to complications with latitude and longitude (definitive), lat and long will be used as reference points in relation to others (easier mapping)
park_1 = Location()
park_1.name = "Blue Ridge Parkway"
park_1.region = "North Carolina and Virgina, United States"
latitude = 36.659089
longitude = -81.077139
park_1.visitors = "15000"
 
session.add(park_1)
session.commit()

park_2 = Location()
park_2.name = "Yellowstone National Park"
park_2.region = "Wyoming, United States"
latitude = 	44.427895
longitude = -110.588379
park_2.visitors = "20000"
 
session.add(park_2)
session.commit()

park_3 = Location()
park_3.name = ""
park_3.region = ", United States"
latitude = 
longitude = 
park_3.visitors = ""
 
session.add(park_3)
session.commit()

park_4 = Location()
park_4.name = ""
park_4.region = ", United States"
latitude = 
longitude = 
park_4.visitors = ""
 
session.add(park_4)
session.commit()

park_5 = Location()
park_5.name = ""
park_5.region = ", United States"
latitude = 
longitude = 
park_5.visitors = ""
 
session.add(park_5)
session.commit()

park_6 = Location()
park_6.name = ""
park_6.region = ", United States"
latitude = 
longitude = 
park_6.visitors = ""
 
session.add(park_6)
session.commit()

park_7 = Location()
park_7.name = ""
park_7.region = ", United States"
latitude = 
longitude = 
park_7.visitors = ""
 
session.add(park_7)
session.commit()

park_8 = Location()
park_8.name = ""
park_8.region = ", United States"
latitude = 
longitude = 
park_8.visitors = ""
 
session.add(park_8)
session.commit()

park_9 = Location()
park_9.name = ""
park_9.region = ", United States"
latitude = 
longitude = 
park_9.visitors = ""
 
session.add(park_9)
session.commit()

park_10 = Location()
park_10.name = ""
park_10.region = ", United States"
latitude = 
longitude = 
park_10.visitors = ""
 
session.add(park_10)
session.commit()

park_11 = Location()
park_11.name = ""
park_11.region = ", United States"
latitude = 
longitude = 
park_11.visitors = ""
 
session.add(park_11)
session.commit()

park_12 = Location()
park_12.name = ""
park_12.region = ", United States"
latitude = 
longitude = 
park_12.visitors = ""
 
session.add(park_12)
session.commit()

park_13 = Location()
park_13.name = ""
park_13.region = ", United States"
latitude = 
longitude = 
park_13.visitors = ""
 
session.add(park_13)
session.commit()

park_14 = Location()
park_14.name = ""
park_14.region = ", United States"
latitude = 
longitude = 
park_14.visitors = ""
 
session.add(park_14)
session.commit()

park_15 = Location()
park_15.name = ""
park_15.region = ", United States"
latitude = 
longitude = 
park_15.visitors = ""
 
session.add(park_15)
session.commit()

##########
###FAUNA##
##########

# adds fauna and provide descriptions of fauna, these can be associated with multiple locations
fauna_black_bear = Fauna()
fauna_black_bear.name = "Black Bear"
fauna_black_bear.characteristics = "A black bear, not brown, not grey, black."

session.add(fauna_black_bear)
session.commit()

fauna_mountain_lion = Fauna()
fauna_mountain_lion.name = "Mountain Lion"
fauna_mountain_lion.characteristics = "A lion that hails from the mountains, but not always."

session.add(fauna_mountain_lion)
session.commit()

###########
###FLORA###
###########

# adds flora and provide descriptions of flora, these can be associated with multiple locations
flora_fir_tree = Flora()
flora_fir_tree.name = "Fir Tree"
flora_fir_tree.characteristics = "Not to be confused with fur."

session.add(flora_fir_tree)
session.commit()

flora_oak_tree = Flora()
flora_oak_tree.name = "Oak Tree"
flora_oak_tree.characteristics = "Strong wood, sometimes of the professor variety of popular franchises."

session.add(flora_oak_tree)
session.commit()

flora_pine_tree = Flora()
flora_pine_tree.name = "Pine Tree"
flora_pine_tree.characteristics = "Smell good, so good that people keep them in cars."

session.add(flora_pine_tree)
session.commit()

##############
###FEATURES###
##############

# adds features and provide descriptions of landmarks/features endemic to each location, these can be associated with specific locations (parks)
feature_ = Feature()
feature_.name = ""
feature_.characteristics = ""

session.add(feature_)
session.commit()

feature_ = Feature()
feature_.name = ""
feature_.characteristics = ""

session.add(feature_)
session.commit()



