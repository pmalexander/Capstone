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
    latitude = Column(Float)
    longitude = Column(Float)
    visitors = Column(Integer)
    overview = Column(String(1024))
    
    def __init__(self, name, region, latitude, longitude, visitors, overview):
        self.name = name
        self.region = region
        self.latitude = name
        self.longitude = region
        self.visitors = name
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

# need to change to streamlined format (all in one line)

################################
###PARKS/RESERVES/WHATHAVEYOU###
################################

#all visitor numbers are placeholders, will probably leave out in later version
# adds national park/reserves to be queried in database, latitude and longitude of location saved
# region (general) was removed due to complications with latitude and longitude (definitive), lat and long will be used as reference points in relation to others (easier mapping)

loc1 = Location('Blue Ridge Parkway', 'North Carolina and Virginia, United States', 36.659089, -81.077139, '15000', 'A park.')
loc2 = Location('Yellowstone National Park', 'Wyoming, United States', 44.427895, -110.588379, '15000', 'A park.')
loc3 = Location('Rothrock State Forest', 'Pennsylvania, United States', 40.720585, -77.826965, '15000', 'A park.')
loc4 = Location('Zion National Park', 'Utah, United States', 37.317207, -113.022537, '15000', 'A park.')
loc5 = Location('Yosemite National Park','California, United States', 37.865101, -119.538330, '15000','A park.')
loc6 = Location('Stanislaus National Forest', 'California, United States', 38.235195, -120.066483, '15000', 'A park.')
loc7 = Location('Haleakala National Park', 'Hawaii, United States', 20.701283, -156.173325, '15000', 'A park.')
loc8 = Location('Malibu Creek State Park', 'California, United States', 34.105156, -118.731316, '15000', 'A park.')
loc9 = Location('Manti-La Sal National Forest', 'Utah, United States', 39.187050, -111.379890, '15000', 'A park.')
loc10 = Location('Cherry Creek State Park','Colorado, United States', 39.639973, -104.831863, '15000', 'A park.')
loc11 = Location('Kissimmee Prairie Preserve State Park', 'Florida, United States', 27.612417, -81.053383, '15000', 'A park.')
loc12 = Location('Garden of Gods', 'Colorado, United States', 38.873840, -104.886665, '15000', 'A park.')
loc13 = Location('Petrified Forest National Park', 'Arizona, United States', 34.909988, -109.806793 , '15000', 'A park.')
loc14 = Location('Chattahoochee National Forest', 'Georgia, United States', 34.765972, -84.143517, '15000', 'A park.')
loc15 = Location('Fort Berthold Indian Reservation', 'North Dakota, United States', 47.683880, -102.354126 , '15000', 'A park.')
loc16 = Location('Yosemite National Park', 'California, United States', 37.8728, -119.573, '15000', 'A park.')
loc17 = Location('Sweetwater Creek State Park', 'Georgia, United States', 33.7525, 84.6287, '15000', 'A park.')

session.add(loc1)
session.add(loc2)
session.add(loc3)
session.add(loc4)
session.add(loc5)
session.add(loc6)
session.add(loc7)
session.add(loc8)
session.add(loc9)
session.add(loc10)
session.add(loc11)
session.add(loc12)
session.add(loc13)
session.add(loc14)
session.add(loc15)
session.add(loc16)
session.add(loc17)

session.commit()

##########
###FAUNA##
##########

# adds fauna and provide descriptions of fauna, these can be associated with multiple locations
# descriptions are not final, just for flavor and fun at the moment until more accurate descriptors (taxonomy and all that) can be issued in a timely manner
# pictures will be provided at a later date, planning on having at least 3 pictures for each entry

#Bears, big and scary ooo
fau1 = Fauna('Black Bear', 'A black bear, not brown, not grey, black. the smallest of the North American bear species.')
fau2 = Fauna('Brown Bear', 'Colloquially known as the Kodiak brown bear, also known as "AGGHHH!!!" when directly encountered, brown bear indeed.')
fau3 = Fauna('Polar Bear', 'This hardy bear survives in the extrmee cold without a coat, scientists are baffled.')

#Birds, owls, hawks, finches, uh... ducks
fau4 = Fauna('Albatross', 'Not a seagull, just an albatross.')
fau5 = Fauna('Brown thresher', 'Do not expect this bird to do your farmwork.')
fau6 = Fauna('Barn Owl', 'Subspecies of owl that like hanging out in barns, or flying into them.' )
fau7 = Fauna('Osprey', 'The largest bird of prey in North America, and its greatest enemy, fish.')

#Big Cats, and just Cats
fau8 = Fauna('Mountain Lion', 'A lion that hails from the mountains, but not always, sometimes from a hill.')

#Deer, deers... dears
fau9 = Fauna('Deer', 'Comes in the white-tailed variety along with moose and elk, neat.')

#Other animals
fau10 = Fauna('Wild Board', 'Two tusks and usually not happy to see you.')

session.add(fau1)
session.add(fau2)
session.add(fau3)
session.add(fau4)
session.add(fau5)
session.add(fau6)
session.add(fau7)
session.add(fau8)
session.add(fau9)
session.add(fau10)

session.commit()

###########
###FLORA###
###########

# adds flora and provide descriptions of flora, these can be associated with multiple locations
# descriptions are not final, just for flavor and fun at the moment until more accurate descriptors (taxonomy and all that) can be issued in a timely manner
#Fruits/Fruit-bearing plants
flora_american_elderberry = Flora()
flora_american_elderberry.name = "American Elderberry"
flora_american_elderberry.characteristics = "Your mother smells of themn."

session.add(flora_american_elderberry)
session.commit()

flora_american_grape = Flora()
flora_american_grape.name = "American Grape"
flora_american_grape.characteristics = "Jam, jelly, wine, good."

session.add(flora_american_grape)
session.commit()

flora_american_mayapple = Flora()
flora_american_mayapple.name = "American Mayapple"
flora_american_mayapple.characteristics = "May or may not be an apple."

session.add(flora_american_mayapple)
session.commit()

flora_american_persimmon = Flora()
flora_american_persimmon.name = "American Persimmon"
flora_american_persimmon.characteristics = "Per simmon of what?"

session.add(flora_american_persimmon)
session.commit()

flora_american_plum = Flora()
flora_american_plum.name = "American Plum"
flora_american_plum.characteristics = "Plum...p fruits that are good and good for you."

session.add(flora_american_plum)
session.commit()

flora_beach_plum = Flora()
flora_beach_plum.name = "Beach Plum"
flora_beach_plum.characteristics = "Beach bum, beach plum, same thing."

session.add(flora_beach_plum)
session.commit()

flora_black_cherry = Flora()
flora_black_cherry.name = "Black Cherry"
flora_black_cherry.characteristics = "It's true, it is sweeter."

session.add(flora_black_cherry)
session.commit()

flora_black_raspberry = Flora()
flora_black_raspberry.name = "Black Raspberry"
flora_black_raspberry.characteristics = "Ditto for these."

session.add(flora_black_raspberry)
session.commit()

flora_blueberry = Flora()
flora_blueberry.name = "Blueberry"
flora_blueberry.characteristics = "They're more purple than blue."

session.add(flora_blueberry)
session.commit()

flora_buffalo_berry = Flora()
flora_buffalo_berry.name = "Buffalo Berry"
flora_buffalo_berry.characteristics = "Doesn't taste like one, I hope."

session.add(flora_buffalo_berry)
session.commit()

flora_canada_plum = Flora()
flora_canada_plum.name = "Canada Plum"
flora_canada_plum.characteristics = "See American plum, just a bit milder."

session.add(flora_canada_plum)
session.commit()

flora_canadian_serviceberry = Flora()
flora_canadian_serviceberry.name = "Canadian Serviceberry"
flora_canadian_serviceberry.characteristics = "Colloquially known as 'sugarplum' ... yeah, I'm confused too."

session.add(flora_canadian_serviceberry)
session.commit()

flora_chokecherry = Flora()
flora_chokecherry.name = "Chokecherry"
flora_chokecherry.characteristics = "Please don't."

session.add(flora_chokecherry)
session.commit()

flora_cocoplum = Flora()
flora_cocoplum.name = "Cocoplum"
flora_cocoplum.characteristics = "Neither coconut or plum, a mystery."

session.add(flora_cocoplum)
session.commit()

flora_concord_grape = Flora()
flora_concord_grape.name = "Concord Grape"
flora_concord_grape.characteristics = "... more jam, jelly, and wine."

session.add(flora_concord_grape)
session.commit()

flora_cranberry = Flora()
flora_cranberry.name = "Cranberry"
flora_cranberry.characteristics = "Grows in the water... should have been called Waterberry."

session.add(flora_cranberry)
session.commit()

flora_dewberry = Flora()
flora_dewberry.name = "Dewberry"
flora_dewberry.characteristics = "Can be mistaken for a blackberry, same family and all that."

session.add(flora_dewberry)
session.commit()

flora_desert_apricot = Flora()
flora_desert_apricot.name = "Desert Apricot"
flora_desert_apricot.characteristics = "Strange, right?"

session.add(flora_desert_apricot)
session.commit()

flora_huckleberry = Flora()
flora_huckleberry.name = "Huckleberry"
flora_huckleberry.characteristics = "Named ones have been to known to exist and take human form."

session.add(flora_huckleberry)
session.commit()

flora_raspberry = Flora()
flora_raspberry.name = "Raspberry"
flora_raspberry.characteristics = "Very tasty, even better if you like chewing on a bunch of seeds."

session.add(flora_raspberry)
session.commit()

flora_strawberry = Flora()
flora_strawberry.name = "Strawberry"
flora_strawberry.characteristics = "The ubiquitous berry, from the vine to your fruit salad or milkshake."

session.add(flora_strawberry)
session.commit()

#Vegetables
flora_corn = Flora()
flora_corn.name = "Corn"
flora_corn.characteristics = "Amazing plant, tastes good roasted, baked, boiled, and popped with a healthy helping of butter. Can be pretty colorful too!"

session.add(flora_corn)
session.commit()

#Trees, just trees
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

flora_abies_amabilis = Flora()
flora_abies_amabilis.name = "Abies Amabilis"
flora_abies_amabilis.characteristics = "A tree."

session.add(flora_abies_amabilis)
session.commit()

flora_abies_bracteata = Flora()
flora_abies_bracteata.name = "Abies Bracteata"
flora_abies_bracteata.characteristics = "A tree."

session.add(flora_abies_bracteata)
session.commit()

flora_abies_fraseri = Flora()
flora_abies_fraseri.name = "Abies Fraseri"
flora_abies_fraseri.characteristics = "A tree."

session.add(flora_abies_fraseri)
session.commit()

############################################# A Tree Index ############################################# 
flora_ = Flora()
flora_.name = "Abies Lasiocarpa"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Abies Magnifica"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Abies Procera"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Acer Macrophyllum"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Acer Negundo"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Acer Pensylvanicum"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Acer Rubrum"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Acer Saccharinum"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Acer Saccharum"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Aesculus Californica"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Ague Tree"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Ahuehuete"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alaska Cedar"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alaska Cypress"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alaska Yellow-cedar"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alaska Yellowcedar"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alaska-cedar"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alaskan Larch"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alberta Spruce"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alberta White Spruce"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Allegheny Chinkapin"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alligator-tree"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Almond Willow"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Almondleaf Willow"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alnus Incana Subspecies Rugosa"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alnus Incana Subspecies Tenuifolia"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alnus Rhombifolia"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alnus Rubra"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alnus Viridis Subspecies Crispa"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alnus Viridis Subspecies Sinuata"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alpine Fir"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alpine Hemlock"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Alpine Larch"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Amabilis Fir"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Amelanchier Arborea"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Basswood"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Beech"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Elm"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Green Alder"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Hackberry"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Holly"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Hophornbeam"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Hornbeam"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Larch"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Mountain-ash"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Plum"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Sycamore"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "American Walnut"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Angelica Tree"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Apache Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Aralia Spinosa"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arbor Vitae"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arborvitae"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arbutus Arizonica"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arbutus Menziesii"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arbutus Texana"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arce - Spanish"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arizona Black Walnut"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arizona Cypress"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arizona Fir"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arizona Longleaf Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arizona Madrone"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arizona Madrono"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arizona Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arizona Rough Cypress"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arizona Walnut"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arizona White Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arkansas Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Arkansas Soft Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Ash-leaved Maple"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Ashe Juniper"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Ashleaf Maple"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Asimina Triloba"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Aspen"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Athel Tamarisk"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Atlantic White-cedar"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Australian-pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Austrian Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

############################################# B Tree Index ############################################# 
flora_ = Flora()
flora_.name = "Baker Cypress"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Baldcypress"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Balsam"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Balsam Fir"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Balsam Fraser Fir"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Balsam Poplar"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Banks Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Banksian Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Barren Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Basket Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Basswood"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bay"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bay Laurel"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Baytree"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Beach Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Beak Willow"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Beaked Willow"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bearberry"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Beaverwood"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bebb Willow"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Beech"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bellota"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Betula Alleghaniensis"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Betula Nigra"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Betula Occidentalis"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Betula Papyrifera"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Betula Populifolia"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Big Drunk Bean"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Big-cone Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Big-laurel"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Big-leaf Maple"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bigcone Douglas-fir"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bigcone Douglas-spruce"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bigcone Spruce"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bigleaf Maple"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bigtooth Aspen"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bigtree"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Biltmore Ash"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Biltmore White Ash"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bishop Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bishop's Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bitter Cherry"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bitternut"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bitternut Hickory"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Birch"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Birck"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Cherry"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Hemlock"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Hills Spruce"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Jack Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Locust"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Myrtle"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Tupelo"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Walnut"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Black Willow"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Blackgum"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Blackjack Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Blisted"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Blister Fir"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Blue Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Blue Paloverde"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Blue Spruce"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Blue-beech"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Blue-poplar"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bluegum"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bluegum Eucalyptus"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bluejack Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bois D'arc"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Border Limber Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Border Pinyon"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Border White Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bottom White Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bottom-land Post Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bottomland Post Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bottomland Red Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Boxelder"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Boynton Post Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bracted Balsam Fir"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Brake Cedar"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Break Cedar"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Brewer Spruce"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bristlecone Fir"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Broadleaf Maple"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Broom Hickory"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Buckeye"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bull Pine"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bull-bay"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bullnut"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Bur Oak"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Butternut"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = "Buttonball Tree"
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = "A tree."

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = "A tree."

session.add(flora_)
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

feature_old_faithful = Feature()
feature_old_faithful.name = "Old Faithful"
feature_old_faithful.characteristics = "An old geyser, spurts reliably, located in Yellowstone National Park."

session.add(feature_old_faithful)
session.commit()

feature_grand_prismatic_spring = Feature()
feature_grand_prismatic_spring.name = "Grand Prismatic Spring"
feature_grand_prismatic_spring.characteristics = "Giant colorful natural spring found in Yellowstone National Park."

session.add(feature_grand_prismatic_spring)
session.commit()

feature_cadillac_mountain = Feature()
feature_cadillac_mountain.name = ""
feature_cadillac_mountain.characteristics = "Not a new car model, but the highes"

session.add(feature_cadillac_mountain)
session.commit()

feature_havasu_falls = Feature()
feature_havasu_falls.name = "Havasu Falls"
feature_havasu_falls.characteristics = "A colorful and scenic diversion found in the Grand Canyon, as well as an opportunity to get wet."

session.add(feature_havasu_falls)
session.commit()

feature_high_dune = Feature()
feature_high_dune.name = "High Dune"
feature_high_dune.hcharacteristics = "No worries about wormsign, the High Dune is 30 miles wide and has some of the highest dunes in North America, it is located in the appropriately named Great Sand Dunes National Park and Preserve."

session.add(feature_high_dune)
session.commit()

feature_harding_icefield_trail = Feature()
feature_harding_icefield_trail.name = "Harding Icefield Trail"
feature_harding_icefield_trail.characteristics = "Pack and prepare for nearly 8 miles of trail on a glacial path at a glacial or not-so glacial pace in Kenjai Fords National Park."

session.add(feature_harding_icefield_trail)
session.commit()

feature_the_narrows = Feature()
feature_the_narrows.name = "The Narrows"
feature_the_narrows.characteristics = "Aptly named as it is the narrowest stretch during your hike in Zion Canyon at the Zion National Park."

session.add(feature_the_narrows)
session.commit()

feature_landscape_arch = Feature()
feature_landscape_arch.name = "Landscape Arch"
feature_landscape_arch.characteristics = "Not falling, nor golden, but a group of naturally formed arches at Arches National Park."

session.add(feature_landscape_arch)
session.commit()

feature_tunnel_view_overlook = Feature()
feature_tunnel_view_overlook.name = "Tunnel View Overlook"
feature_tunnel_view_overlook.characteristics = "A good view of Yosemite National Park's other attractions, Half Dome, Bridalveil Fall and El Capitan."

session.add(feature_tunnel_view_overlook)
session.commit()

feature_general_sherman_tree = Feature()
feature_general_sherman_tree.name = "The General Sherman Tree"
feature_general_sherman_tree.characteristics = "Unlike Union Army general of its namesake, this tree does not appreciate fire, but is also a historical standout in being the largest tree in the world, located right in Sequoia National Park."

session.add(feature_general_sherman_tree)
session.commit()

feature_crater_lake = Feature()
feature_crater_lake.name = "Crater Lake"
feature_crater_lake.characteristics = "Just as the name implies, it's a crater lake. Formed by an eruption from a now inactive volcano a long, long, long, time ago, to be the deepest lake in the United States. Located in the appropirately named Crater Lake National Park."

session.add(feature_crater_lake)
session.commit()

feature_highline_trail = Feature()
feature_highline_trail.name = "Highline Trail"
feature_highline_trail.characteristics = "A high-elevation trail in Glacier National Park, with a good view of the mountain peaks and valleys, unless you're acrophobic, in which case it gives a good view of fear."

session.add(feature_highline_trail)
session.commit()

feature_mount_kilauea = Feature()
feature_mount_kilauea.name = "Mount Kilauea"
feature_mount_kilauea.characteristics = "This notorious and extremely volatile active volcano is located in the Hawaii Volcanoes National Park, busy producing up to 500,000 cubic meters of lava per day. Don't get too close."

session.add(feature_mount_kilauea)
session.commit()

feature_hoh_rain_forest = Feature()
feature_hoh_rain_forest.name = "Hoh Rain Forest"
feature_hoh_rain_forest.characteristics = "Figured your compass turned you wrong? Nope, this rainforest is a part of Olympic National Park's attractions, representative of a temperate rainforest biome located in North America."

session.add(feature_hoh_rain_forest)
session.commit()

feature_bryce_amphitheater = Feature()
feature_bryce_amphitheater.name = "Bryce Amphitheater"
feature_bryce_amphitheater.characteristics = "A 6-mile stretch of Bryce Canyon National Park features a series of spires, eerily colorful a different points of the day, and invoking the image of a crowd of individuals standing shoulder to shoulder."

session.add(feature_bryce_amphitheater)
session.commit()

''' template for feature

feature_ = Feature()
feature_.name = ""
feature_.characteristics = ""

session.add(feature_)
session.commit()

'''