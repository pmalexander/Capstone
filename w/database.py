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
   
    loc_id = Column(Integer, ForeignKey(Location.id), nullable=True)

# same with flora, flora is not exclusive to a single location, some places may not have flora in the same range
class Flora(Base):
    __tablename__ = "flora"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    
    loc_id = Column(Integer, ForeignKey(Location.id), nullable=True)

# certain landmarks are endemic to specific sites, many can exist in one site
class Feature(Base):
    __tablename__ = "features"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
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
park_1.latitude = 36.659089
park_1.longitude = -81.077139
park_1.visitors = "15000"
 
session.add(park_1)
session.commit()

park_2 = Location()
park_2.name = "Yellowstone National Park"
park_2.region = "Wyoming, United States"
park_2.latitude = 44.427895
park_2.longitude = -110.588379
park_2.visitors = "15000"
 
session.add(park_2)
session.commit()

park_3 = Location()
park_3.name = "Rothrock State Forest"
park_3.region = "Pennsylvania, United States"
park_3.latitude = 40.720585
park_3.longitude = -77.826965
park_3.visitors = "15000"
 
session.add(park_3)
session.commit()

park_4 = Location()
park_4.name = "Zion National Park"
park_4.region = "Utah, United States"
park_4.latitude = 37.317207
park_4.longitude = -113.022537
park_4.visitors = "15000"
 
session.add(park_4)
session.commit()

park_5 = Location()
park_5.name = "Yosemite National Park"
park_5.region = "California, United States"
park_5.latitude = 37.865101
park_5.longitude = -119.538330
park_5.visitors = "15000"
 
session.add(park_5)
session.commit()

park_6 = Location()
park_6.name = "Stanislaus National Forest"
park_6.region = "California, United States"
park_6.latitude = 38.235195
park_6.longitude = -120.066483
park_6.visitors = "15000"
 
session.add(park_6)
session.commit()

park_7 = Location()
park_7.name = "Haleakala National Park"
park_7.region = " Hawaii, United States"
park_7.latitude = 20.701283
park_7.longitude = -156.173325
park_7.visitors = "15000"
 
session.add(park_7)
session.commit()

park_8 = Location()
park_8.name = "Malibu Creek State Park"
park_8.region = "California, United States"
park_8.latitude = 34.105156
park_8.longitude = -118.731316
park_8.visitors = "15000"
 
session.add(park_8)
session.commit()

park_9 = Location()
park_9.name = "Manti-La Sal National Forest"
park_9.region = "Utah, United States"
park_9.latitude = 39.187050
park_9.longitude = -111.379890
park_9.visitors = "15000"
 
session.add(park_9)
session.commit()

park_10 = Location()
park_10.name = "Cherry Creek State Park"
park_10.region = "Colorado, United States"
park_10.latitude = 39.639973
park_10.longitude = -104.831863
park_10.visitors = "15000"
 
session.add(park_10)
session.commit()

park_11 = Location()
park_11.name = "Kissimmee Prairie Preserve State Park"
park_11.region = "Florida, United States"
park_11.latitude = 27.612417
park_11.longitude = -81.053383
park_11.visitors = "15000"
 
session.add(park_11)
session.commit()

park_12 = Location()
park_12.name = "Garden of Gods"
park_12.region = "Colorado, United States"
park_12.latitude = 38.873840
park_12.longitude = -104.886665
park_12.visitors = "15000"
 
session.add(park_12)
session.commit()

park_13 = Location()
park_13.name = "Petrified Forest National Park"
park_13.region = "Arizona, United States"
park_13.latitude = 34.909988
park_13.longitude = -109.806793 
park_13.visitors = "15000"
 
session.add(park_13)
session.commit()

park_14 = Location()
park_14.name = "Chattahoochee National Forest"
park_14.region = "Georgia, United States"
park_14.latitude = 34.765972 
park_14.longitude = -84.143517
park_14.visitors = "15000"
 
session.add(park_14)
session.commit()

park_15 = Location()
park_15.name = "Fort Berthold Indian Reservation"
park_15.region = "North Dakota, United States"
park_15.latitude = 47.683880
park_15.longitude = -102.354126 
park_15.visitors = "15000"
 
session.add(park_15)
session.commit()

'''dummied out as a template
park_ = Location()
park_.name = ""
park_.region = ""
latitude =
longitude =
park_.visitors = ""
 
session.add(park_)
session.commit()
'''

##########
###FAUNA##
##########

# adds fauna and provide descriptions of fauna, these can be associated with multiple locations
# descriptions are not final, just for flavor and fun at the moment until more accurate descriptors (taxonomy and all that) can be issued in a timely manner
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

fauna_deer = Fauna()
fauna_deer.name = "Deer"
fauna_deer.characteristics = "Comes in the white-tailed variety along with moose and elk, neat."

session.add(fauna_deer)
session.commit()

fauna_wild_boar = Fauna()
fauna_wild_boar.name = "Wild Boar"
fauna_wild_boar.characteristics = "Two tusks and usually not happy to see you."

session.add(fauna_wild_boar)
session.commit()

fauna_barn_owl = Fauna()
fauna_barn_owl.name = "Barn Owl"
fauna_barn_owl.characteristics = "Subspecies of owl that like hanging out in barns, or flying into them."

session.add(fauna_barn_owl)
session.commit()

'''dummied out as a template
fauna_ = Fauna()
fauna_.name = ""
fauna_.characteristics = ""

session.add(fauna_)
session.commit()
'''

###########
###FLORA###
###########

# adds flora and provide descriptions of flora, these can be associated with multiple locations
# descriptions are not final, just for flavor and fun at the moment until more accurate descriptors (taxonomy and all that) can be issued in a timely manner
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

flora_blueberry = Flora()
flora_blueberry.name = "Blueberry"
flora_blueberry.characteristics = "They're more purple than blue."

session.add(flora_blueberry)
session.commit()

flora_raspberry = Flora()
flora_raspberry.name = "Raspberry"
flora_raspberry.characteristics = "Very tasty, even better if you like chewing on a bunch of seeds."

session.add(flora_raspberry)
session.commit()

flora_corn = Flora()
flora_corn.name = "Corn"
flora_corn.characteristics = "Amazing plant, tastes good roasted, baked, boiled, and popped with a healthy helping of butter. Can be pretty colorful too!"

session.add(flora_corn)
session.commit()

'''dummied out as template
flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

session.add(flora_)
session.commit()
'''

##############
###FEATURES###
##############

# adds features and provide descriptions of landmarks/features endemic to each location, these can be associated with specific locations (parks)
# descriptions are not final, just for flavor and fun at the moment until more accurate descriptors (taxonomy, attractions, natural formations, historical creations and all that) can be issued in a timely manner
feature_petrified_wood = Feature()
feature_petrified_wood.name = "Petrified Wood"
feature_petrified_wood.characteristics = "Really hard and really old wood endemic, but not exclusive to, the Petrified Forest National Park "

session.add(feature_petrified_wood)
session.commit()

feature_balanced_rock = Feature()
feature_balanced_rock.name = "Balanced Rock"
feature_balanced_rock.characteristics = "A precariously placed (by nature) rock that sits atop another rock in Garden of the Gods, don't sleep underneath it."

session.add(feature_balanced_rock)
session.commit()

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

feature_ = Feature()
feature_.name = ""
feature_.characteristics = ""

session.add(feature_)
session.commit()


