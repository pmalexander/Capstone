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
    # one flora to many locations
    flora_id = Column(Integer, ForeignKey("Flora.id"))
    # many landmarks to one location
    features = relationship("Feature", backref="location_features")
    
class Fauna(Base):
    __tablename__ = "fauna"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    location_fauna = relationship("Location", backref="locations")
    assoc_fauna = relationship("Location", backref="assoc_fauna")
    loc_id = Column(Integer, ForeignKey(Location.id, nullable=False))

class Flora(Base):
    __tablename__ = "flora"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    assoc_flora = relationship("Location", backref="assoc_flora")
    loc_id = Column(Integer, ForeignKey(Location.id, nullable=False))
    
class Feature(Base):
    __tablename__ = "features"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    loc_id = Column(Integer, ForeignKey(Location.id, nullable=False))
    assoc_feature = relationship("Location", backref="assoc_feature")
    
    # there are multiple UNIQUE landmarks in one location, so this is many to one
    location = Column(Integer, ForeignKey("locations.id"))
    
class User(Base, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))
    
class Inventory(Base):
    __tablename__ = "inventory"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    characteristics = Column((String)(1024))

# creates the database, everything following up is what will be loaded into the database
Base.metadata.create_all(engine)

###need to change to streamlined format (all in one line)
#adds national park/reserves to be queried in database, latitude and longitude of location saved
#region (general) was removed due to complications with latitude and longitude (definitive), lat and long will be used as reference points in relation to others (easier mapping)
park_1 = Location()
park_1.name = "Blue Ridge Parkway"
park_1.region = "North Carolina and Virgina, United States"
latitude = 36.659089
longitude = -81.077139
park_1.visitors = "15000"
 
session.add(park_1)
session.commit()

#adds fauna and provide descriptions of fauna, these can be associated with specific locations
fauna_black_bear = Fauna()
fauna_black_bear.name = "Black Bear"
fauna_black_bear.description = "They are often found in areas with relatively inaccessible terrain, thick understory vegetation and large quantities of edible material (especially masts). The adaptation to woodlands and thick vegetation in this species may have originally been due to the black bear having evolved alongside larger, more aggressive bear species, such as the extinct short-faced bear and the still living grizzly bear, that monopolized more open habitats and the historic presence of larger predators such as smilodon and the American lion that could have preyed on black bears. Although found in the largest numbers in wild, undisturbed areas and rural regions, black bears can adapt to surviving in some numbers in peri-urban regions as long as they contain easily accessible foods and some vegetative coverage."

session.add(black_bear)
session.commit()

#adds flora and provide descriptions of flora, these can be associated with specific locations
flora_fir_tree = Flora()
flora_fir_tree.name = "Fir Tree"
flora_fir_tree.characteristics = "Firs are most closely related to the genus Cedrus (cedar). Douglas firs are not true firs, being of the genus Pseudotsuga. hey are large trees, reaching heights of 10–80 m (33–262 ft) tall and trunk diameters of 0.5–4 m (1 ft 8 in–13 ft 1 in) when mature. Firs can be distinguished from other members of the pine family by the unique attachment of their needle-like leaves and by their different cones."

session.add(black_bear)
session.commit()

#adds features and provide descriptions of landmarks/features endemic to each location, these can be associated with specific locations (parks)
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



