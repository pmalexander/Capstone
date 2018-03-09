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
    region = Column((String)(1024))
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

park_16 = Location()
park_16.name = "Yosemite National Park"
park_16.region = "California, United States"
park_16.latitude = 37.8728
park_16.longitude = -119.573
park_16.visitors = "15000"
 
session.add(park_16)
session.commit()

'''
park_17 = Location()
park_17.name = ""
park_17.region = ", United States"
park_17.latitude = 
park_17.longitude = 
park_17.visitors = "15000"
 
session.add(park_17)
session.commit()

park_18 = Location()
park_18.name = ""
park_18.region = ""
park_18.latitude = 
park_18.longitude = -
park_18.visitors = "15000"
 
session.add(park_18)
session.commit()

park_19 = Location()
park_19.name = ""
park_19.region = ""
park_19.latitude = 
park_19.longitude = -
park_19.visitors = ""
 
session.add(park_19)
session.commit()

park_20 = Location()
park_20.name = ""
park_20.region = ", United States"
park_20.latitude = 
park_20.longitude = 
park_20.visitors = "15000"
 
session.add(park_20)
session.commit()

park_21 = Location()
park_21.name = ""
park_21.region = ", United States"
park_21.latitude = 
park_21.longitude =  
park_21.visitors = "15000"
 
session.add(park_21)
session.commit()

park_22 = Location()
park_22.name = ""
park_22.region = ", United States"
park_22.latitude = 
park_22.longitude = 
park_22.visitors = "15000"
 
session.add(park_22)
session.commit()

park_23 = Location()
park_23.name = ""
park_23.region = ", United States"
park_23.latitude = 
park_23.longitude = 
park_23.visitors = "15000"
 
session.add(park_23)
session.commit()

park_24 = Location()
park_24.name = ""
park_24.region = ", United States"
park_24.latitude = 
park_24.longitude = 
park_24.visitors = "15000"
 
session.add(park_24)
session.commit()

park_25 = Location()
park_25.name = ""
park_25.region = ", United States"
park_25.latitude = 
park_25.longitude = 
park_25.visitors = "15000"
 
session.add(park_25)
session.commit()

park_26 = Location()
park_26.name = ""
park_26.region = ", United States"
park_26.latitude = 
park_26.longitude = 
park_26.visitors = "15000"
 
session.add(park_26)
session.commit()

park_27 = Location()
park_27.name = "n"
park_27.region = ", United States"
park_27.latitude = 
park_27.longitude = 
park_27.visitors = "15000"
 
session.add(park_27)
session.commit()

park_28 = Location()
park_28.name = ""
park_28.region = ", United States"
park_28.latitude = 
park_28.longitude = 
park_28.visitors = "15000"
 
session.add(park_28)
session.commit()

park_29 = Location()
park_29.name = ""
park_29.region = ", United States"
park_29.latitude = 
park_29.longitude = 
park_29.visitors = "15000"
 
session.add(park_29)
session.commit()

park_30 = Location()
park_30.name = ""
park_30.region = ", United States"
park_30.latitude = 
park_30.longitude = 
park_30.visitors = "15000"
 
session.add(park_30)
session.commit()

dummied out as a template
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
# pictures will be provided at a later date, planning on having at least 3 pictures for each entry

#Bears, big and scary ooo
fauna_black_bear = Fauna()
fauna_black_bear.name = "Black Bear"
fauna_black_bear.characteristics = "A black bear, not brown, not grey, black. the smallest of the North American bear species."

session.add(fauna_black_bear)
session.commit()

fauna_brown_bear = Fauna()
fauna_brown_bear.name = "Brown Bear"
fauna_brown_bear.characteristics = "Colloquially known as the Kodiak brown bear, also known as 'AGGHHH!!!' when directly encountered, brown bear indeed."

session.add(fauna_brown_bear)
session.commit()

fauna_polar_bear = Fauna()
fauna_polar_bear.name = "Polar Bear"
fauna_polar_bear.characteristics = "This hardy bear survives in the extrmee cold without a coat, scientists are baffled."

session.add(fauna_polar_bear)
session.commit()

#Birds, owls, hawks, finches, uh... ducks
fauna_albatross = Fauna()
fauna_albatross.name = "Albatross"
fauna_albatross.characteristics = "Not a seagull, just an albatross."

session.add(fauna_albatross)
session.commit()

fauna_brown_thresher = Fauna()
fauna_brown_thresher.name = "Brown thresher"
fauna_brown_thresher.characteristics = "Don't expect this bird to do your farmwork."

session.add(fauna_brown_thresher)
session.commit()

fauna_barn_owl = Fauna()
fauna_barn_owl.name = "Barn Owl"
fauna_barn_owl.characteristics = "Subspecies of owl that like hanging out in barns, or flying into them."

session.add(fauna_barn_owl)
session.commit()

fauna_osprey = Fauna()
fauna_osprey.name = "Osprey"
fauna_osprey.characteristics = "The largest bird of prey in North America, and its greatest enemy, fish."

#Big Cats, and just Cats
fauna_mountain_lion = Fauna()
fauna_mountain_lion.name = "Mountain Lion"
fauna_mountain_lion.characteristics = "A lion that hails from the mountains, but not always, sometimes from a hill."

session.add(fauna_mountain_lion)
session.commit()

#Deer, deers... dears
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

fauna_ = Fauna()
fauna_.name = ""
fauna_.characteristics = ""

session.add(fauna_)
session.commit()

fauna_ = Fauna()
fauna_.name = ""
fauna_.characteristics = ""

session.add(fauna_)
session.commit()

fauna_ = Fauna()
fauna_.name = ""
fauna_.characteristics = ""

session.add(fauna_)
session.commit()

fauna_ = Fauna()
fauna_.name = ""
fauna_.characteristics = ""

session.add(fauna_)
session.commit()

fauna_ = Fauna()
fauna_.name = ""
fauna_.characteristics = ""

session.add(fauna_)
session.commit()

fauna_ = Fauna()
fauna_.name = ""
fauna_.characteristics = ""

session.add(fauna_)
session.commit()

fauna_ = Fauna()
fauna_.name = ""
fauna_.characteristics = ""

session.add(fauna_)
session.commit()

fauna_ = Fauna()
fauna_.name = ""
fauna_.characteristics = ""

session.add(fauna_)
session.commit()

fauna_ = Fauna()
fauna_.name = ""
fauna_.characteristics = ""

session.add(fauna_)
session.commit()

fauna_ = Fauna()
fauna_.name = ""
fauna_.characteristics = ""

session.add(fauna_)
session.commit()

fauna_ = Fauna()
fauna_.name = ""
fauna_.characteristics = ""

session.add(fauna_)
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

flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

session.add(flora_)
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

'''
Abies Amabilis
Abies Balsamea
Abies Bracteata
Abies Fraseri
Abies Lasiocarpa
Abies Magnifica
Abies Procera
Acer Macrophyllum
Acer Negundo
Acer Pensylvanicum
Acer Rubrum
Acer Saccharinum
Acer Saccharum
Aesculus Californica
Ague Tree
Ahuehuete
Alaska Cedar
Alaska Cypress
Alaska Yellow-cedar
Alaska Yellowcedar
Alaska-cedar
Alaskan Larch
Alberta Spruce
Alberta White Spruce
Allegheny Chinkapin
Alligator-tree
Almond Willow
Almondleaf Willow
Alnus Incana Subsp. Rugosa
Alnus Incana Subsp. Tenuifolia
Alnus Rhombifolia
Alnus Rubra
Alnus Viridis Subsp. Crispa
Alnus Viridis Subsp. Sinuata
Alpine Fir
Alpine Hemlock
Alpine Larch
Amabilis Fir
Amelanchier Arborea
American Basswood
American Beech
American Elm
American Green Alder
American Hackberry
American Holly
American Hophornbeam
American Hornbeam
American Larch
American Mountain-ash
American Plum
American Sycamore
American Walnut
Angelica Tree
Apache Pine
Aralia Spinosa
Arbor Vitae
Arborvitae
Arbutus Arizonica
Arbutus Menziesii
Arbutus Texana
Arce (Spanish)
Arizona Black Walnut
Arizona Cypress
Arizona Fir
Arizona Longleaf Pine
Arizona Madrone
Arizona Madrono
Arizona Oak
Arizona Rough Cypress
Arizona Walnut
Arizona White Oak
Arkansas Pine
Arkansas Soft Pine
Ash-leaved Maple
Ashe Juniper
Ashleaf Maple
Asimina Triloba
Aspen
Athel Tamarisk
Atlantic White-cedar
Australian-pine
Austrian Pine

Baker Cypress
Baldcypress
Balsam
Balsam Fir
Balsam Fraser Fir
Balsam Poplar
Banks Pine
Banksian Pine
Barren Oak
Basket Oak
Basswood
Bay
Bay Laurel
Baytree
Beach Pine
Beak Willow
Beaked Willow
Bearberry
Beaverwood
Bebb Willow
Beech
Bellota
Betula Alleghaniensis
Betula Nigra
Betula Occidentalis
Betula Papyrifera
Betula Populifolia
Big Drunk Bean
Big-cone Pine
Big-laurel
Big-leaf Maple
Bigcone Douglas-fir
Bigcone Douglas-spruce
Bigcone Spruce
Bigleaf Maple
Bigtooth Aspen
Bigtree
Biltmore Ash
Biltmore White Ash
Bishop Pine
Bishop's Pine
Bitter Cherry
Bitternut
Bitternut Hickory
Black Birch
Black Birck
Black Cherry
Black Hemlock
Black Hills Spruce
Black Jack Oak
Black Locust
Black Myrtle
Black Oak
Black Pine
Black Tupelo
Black Walnut
Black Willow
Blackgum
Blackjack Oak
Blisted
Blister Fir
Blue Oak
Blue Paloverde
Blue Spruce
Blue-beech
Blue-poplar
Bluegum
Bluegum Eucalyptus
Bluejack Oak
Bois D'arc
Border Limber Pine
Border Pinyon
Border White Pine
Bottom White Pine
Bottom-land Post Oak
Bottomland Post Oak
Bottomland Red Oak
Boxelder
Boynton Post Oak
Bracted Balsam Fir
Brake Cedar
Break Cedar
Brewer Spruce
Bristlecone Fir
Broadleaf Maple
Broom Hickory
Buckeye
Bull Pine
Bull-bay
Bullnut
Bur Oak
Butternut
Buttonball Tree

Cabbage Palmetto
California Bay
California Black Walnut
California Blue Oak
California Boxelder
California Buckeye
California Coulter Pine
California Fan Palm
California Filbert
California Hazel
California Hazelnut
California Juniper
California Laurel
California Nutmeg
California Palm
California Red Fir
California Redwood
California Swamp Pine
California Torreya
California Walnut
California Washington-palm
California White Oak
Calocedrus Decurrens
Cambria Pine
Canada Balsam
Canada Hemlock
Canadian Balsam
Canadian Spruce
Cane Ash
Canoe Birch
Canoe-cedar
Canyon Live Oak
Carolina Beech
Carolina Hemlock
Carpinus Caroliniana
Carya Cordiformis
Carya Glabra
Carya Illinoensis
Carya Ovata
Carya Tomentosa
Cascades Fir
Castanea Pumila
Casuarina Spp.
Cat Spruce
Caudate Willow
Cedar Pine
Cedro
Cedro Blanco
Cedro De La Sierra
Cedros Island Pine
Celtis Laevigata
Celtis Occidentalis
Celtis Reticulata
Cercidium Floridum
Cercis Canadensis
Chamaecyparis Lawsoniana
Chamaecyparis Nootkatensis
Chamaecyparis Thyoides
Chaton
Cherioni
Cherrion
Cherrybark Oak
Chestnut Oak
Chihuahua Pine
Chinaberry
Chinkapin
Chinkapin Oak
Chinquapin
Chinquapin Oak
Chrysolepis Chrysophylla
Cinnamon Bush
Cinnamon Oak
Cinnamon Wood
Cipres
Ciruela
Coast Douglas-fir
Coast Pignut Hickory
Coast Pine
Coast Redwood
Coast Spruce
Coastal Laurel Oak
Colorado Blue Spruce
Colorado Spruce
Colorin
Columbian Spruce
Common Hackberry
Common Honey-locust
Common Larch
Common Persimmon
Common Red Oak
Common Sassafras
Coos Bay Laurel
Copalm Balsam
Coral Bean
Coralbean
Cork-bark Fir
Corkbark Fir
Cormier (Quebec)
Cornus Racemosa
Corsican Pine
Corylus Cornuta Var. Californica
Coulter Pine
Cow Oak
Crataegus Douglasii
Crimean Pine
Cross Oak
Cuban Pine
Cunningham Casuarina
Cupressus Bakeri
Cupressus Forbesii
Cupressus Goveniana
Cupressus Macnabiana
Cupressus Macrocarpa
Cupressus Sargentii
Curtiss Possumhaw
Custard Apple
Cypress

Dade County Pine
Dade County Slash Pine
Darlington Oak
Deciduous Holly
Del Mar Pine
Delta Post Oak
Desert Fir
Desert Palm
Desert White Cedar
Devil's Walking Stick
Diamond Willow
Diamond-leaf Oak
Diospyros Texana
Diospyros Virginiana
Dog Banana
Dogberry
Douglas-fir
Downy Serviceberry
Drummond Post Oak
Drummond Soapberry
Duck Oak
Dudley Willow
Dune Holly
Dwarf Canyon Live Oak
Dwarf Interior Live Oak
Dwarf Post Oak
Dwarf Walnut

Eastern Arborvitae
Eastern Black Walnut
Eastern Fir
Eastern Hemlock
Eastern Hophornbeam
Eastern Larch
Eastern Persimmon
Eastern Red Oak
Eastern Red Pine
Eastern Redbud
Eastern Spruce
Eastern White Pine
Eastern White-cedar
Elliott Oak
Emory Oak
Enebro
Engelmann Spruce
Eucalyptus Globulus
European Black Pine
European Larch
European Speckled Alder
European Spruce
Evergreen Coralbean
Evergreen Magnolia

Fagus Grandifolia
False Acacia
False Cypress
False Elm
False Hemlock
False Shagbark
False-banana
False-cedar
Fetid-shrub
Fire Birch
Florida Elm
Florida Persimmon
Florida Torreya
Florida Yew
Foothills Pine
Forbes Cypress
Fork-leaf Oak
Forked-leaf White Oak
Four-needled Pinyon
Fraser Fir
Fraser's Fir
Fraxinus Americana
Fresno De Guajuco (Spanish)
Frigolito
Frijolillo
Frijolito
Frijollito

Giant Arborvitae
Giant Chinkapin
Giant Chinquapin
Giant Evergreen Chinkapin
Giant Evergreen-chinkapin
Giant Redcedar
Giant Sequoia
Ginger Pine
Glaucous Willow
Gleditsia Triacanthos
Golden Chinkapin
Golden Fir
Golden Willow
Goldenleaf Chestnut
Goodding Willow
Goosefoot Maple
Gopherwood
Gordonia
Gordonia Lasianthus
Gowen Cypress
Gray Alder
Gray Beech
Gray Birch
Gray Dogwood
Gray Elm
Gray Oak
Gray Pine
Gray Willow
Gray-leaved Willow
Gray-stemmed Dogwood
Grayleaf Willow
Green Alder
Green Locust
Grey Birch
Grey Dogwood
Grey Oak
Grey Sheoak
Guadalupe Island Pine
Gulf Black Willow
Gulf Cypress
Gum-wood
Gumbo File

Hackberry
Hackmatack
Hamamelis Virginiana
Hard Maple
Hazel Alder
He-balsam
Hedge-apple
Hemlock
Hemlock Spruce
Hercules Club
Hickory Pine
Highland Live Oak
Hill's Oak
Hoary Alder
Hognut
Hojalito
Holly Bay
Honey Shucks Locust
Honey-locust
Hophornbeam
Horestail Casuarina
Horsechestnut
Hudson Bay Pine
Hummock Holly

Idaho White Pine
Ilex Decidua
Ilex Opaca
Illinois Nut
Incense-cedar
Indian Banana
Indian Soap Plant
Inland Boxelder
Insignis Pine
Interior Live Oak
Iron Oak
Ironwood

Jaboncillo
Jack Oak
Jack Pine
Jeffrey Pine
Jersey Pine
Judas-tree
Juglans Californica
Juglans Cinerea
Juglans Major
Juglans Microcarpa
Juglans Nigra
Juneberry
Juniper
Juniperus Ashei
Juniperus Californica
Juniperus Coahuilensis

Knobcone Pine
Knowlton Hophornbeam

Lady Legs
Lady's Legs
Larch
Large-flower Magnolia
Largetooth Aspen
Larix Decidua
Larix Laricina
Larix Lyallii
Laurel
Laurel Magnolia
Laurel Oak
Laurel-leaf Oak
Lawson Cypress
Lawson False-cypress
Lily-of-the-valley-tree
Linden
Liquidambar Styraciflua
Liriodendron Tulipifera
Lithocarpus Densiflorus
Little Walnut
Live Oak
Loblolly Pine
Loblolly-bay
Locust
Lodgepole Pine
Long-beaked Willow
Longleaf Casuarina
Lovely Fir
Lowland Hackberry
Lyall Larch
Lyall's Larch

MacNab Cypress
Maclura Pomifera
Madrona
Madrone
Madrono
Magnolia Grandiflora
Magnolia Virginiana
Manitoba Maple
Manzanita
Maul Oak
Menzies' Spruce
Mescal Bean
Mescal-bean Sophora
Mescalbean Sophora
Mexican Blue Oak
Mexican Juniper
Mexican Persimmon
Mexican Pinyon
Mexican Soapberry
Mexican Walnut
Mexican White Pine
Missey-mossey
Mississippi Valley Oak
Mitten Tree
Mockernut
Mockernut Hickory
Modoc Cypress
Monterey Cypress
Monterey Pine
Montezuma Baldcypress
Moosewood
Moral
Morus Rubra
Mossy-overcup Oak
Mossycup Oak
Mountain Alder
Mountain Ash
Mountain Birch
Mountain Black Cherry
Mountain Cedar
Mountain Cypress
Mountain Hemlock
Mountain Laurel
Mountain Mahogany
Mountain Oak
Mountain Pine
Mountain Red Oak
Mountain Spruce
Mountain White Oak
Mountain White Pine
Mulberry
Muscletree
Myrtle
Myrtletree
Myrtlewood

Naked Indian
Namboca
Netleaf Hackberry
Nettletree
New Mexican Locust
New Mexico Locust
Noble Fir
Nogal
Nogalillo
Nogalito
Nootka Cypress
Nootka False-cypress
North Carolina Pine
Northern Hackberry
Northern Pin Oak
Northern Pine
Northern Red Oak
Northern Scrub Pine
Northern White Cedar
Northern White Pine
Northern White-cedar
Norway Pine
Norway Spruce
Nut Pine
Nuzu-ndu
Nyssa Sylvatica

Obtusa Oak
Oilnut
Old Field Pine
Oldfield Birch
Oldfield Pine
Opossum-tree
Orange Oak
Oregon Alder
Oregon Douglas-fir
Oregon Maple
Oregon Myrtle
Oregon-cedar
Osage-orange
Ostrya Knowltonii
Ostrya Virginiana
Overcup Oak
Oxydendrum Arboreum
Ozark Chinkapin
Ozark White Cedar

Pacific Coast Alder
Pacific Hemlock
Pacific Madrone
Pacific Myrtle
Pacific Ponderosa Pine
Pacific Redcedar
Pacific Silver Fir
Pacific Willow
Pacific Yew
Palo Blanco
Panicled Dogwood
Paper Birch
Papershell Pinyon
Parry Pinyon
Pawpaw
Pawpaw-apple
Peach Oak
Peach Willow
Peach-leaved Willow
Peachleaf Willow
Pecan
Pecan Hickory
Pentamon
Pepperidge
Pepperwood
Persea Borbonia
Persimmon
Petit Minou
Picea Abies
Picea Breweriana
Picea Engelmannii
Picea Glauca
Picea Pungens
Picea Rubens
Picea Sitchensis
Pick Tree
Pignut
Pignut Hickory
Pin Blanc
Pin Oak
Pino Enano
Pino Real
Pino Real Blanco
Pinobete
Pinus Attenuata
Pinus Banksiana
Pinus Cembroides
Pinus Clausa
Pinus Contorta Var. Contorta
Pinus Contorta Var. Murrayana
Pinus Coulteri
Pinus Echinata
Pinus Elliottii
Pinus Engelmannii
Pinus Glabra
Pinus Jeffreyi
Pinus Lambertiana
Pinus Leiophylla Var. Chihuahuana
Pinus Monticola
Pinus Muricata
Pinus Nigra
Pinus Ponderosa Var. Ponderosa
Pinus Pungens
Pinus Quadrifolia
Pinus Radiata
Pinus Resinosa
Pinus Sabiniana
Pinus Strobiformis
Pinus Strobus
Pinus Sylvestris
Pinus Taeda
Pinus Torreyana
Pinus Virginiana
Pinus Washoensis
Pitch Pine
Plane Tree
Platanus Occidentalis
Polecat Wood
Pondcypress
Ponderosa Pine
Populus Balsamifera
Populus Grandidentata
Populus Tremuloides
Porsild Spruce
Port Orford-cedar
Port-Orford White-cedar
Port-Orford-cedar
Possum Oak
Possum Pine
Possumhaw
Possumwood
Post Cedar
Post Locust
Post Oak
Pottawattami Plum
Poverty Pine
Prickle-cone Pine
Prickly Ash
Prickly Elder
Prickly Pine
Princess Pine
Prosopis Velutina
Prunus Americana
Prunus Emarginata
Prunus Serotina
Pseudotsuga Macrocarpa
Pseudotsuga Menziesii Var. Menziesii
Punk Oak
Pyrenees Pine

Quaking Aspen
Quercitron
Quercitron Oak
Quercus Alba
Quercus Arizonica
Quercus Bicolor
Quercus Chrysolepis
Quercus Coccinea
Quercus Douglasii
Quercus Ellipsoidalis
Quercus Emoryi
Quercus Falcata
Quercus Grisea
Quercus Incana
Quercus Laurifolia
Quercus Lobata
Quercus Lyrata
Quercus Macrocarpa
Quercus Marilandica
Quercus Michauxii
Quercus Muehlenbergii
Quercus Nigra
Quercus Oblongifolia
Quercus Palustris
Quercus Phellos
Quercus Prinus
Quercus Pungens
Quercus Rubra
Quercus Shumardii
Quercus Stellata
Quercus Velutina
Quercus Virginiana
Quercus Wislizenii

Radiata Pine
Red Alder
Red Bean
Red Beech
Red Birch
Red Cypress
Red Elm
Red Fir
Red Hickory
Red Maple
Red Mulberry
Red Oak
Red Pine
Red Plum
Red Spruce
Red Willow
Red-hots
Redbay
Redberry Juniper
Redbud
Redgum
Redwood
Rhus Typhina
Ridge Beech
Ridge White Oak
River Alder
River Birch
River Plum
River Sheoak
River Walnut
River-oak
Robinia Neomexicana
Robinia Pseudoacacia
Roble
Rock Cedar
Rock Chestnut Oak
Rock Maple
Rock Oak
Rocky Mountain Birch
Rocky Mountain Fir
Rose-fruited Juniper
Rough-bark Cypress
Roundwood
Rum Cherry
Runner Oak

Sabal Palmetto
Sabino
Salix Amygdaloides
Salix Bebbiana
Salix Glauca
Salix Gooddingii
Salix Lasiandra
Salix Lutea
Salix Nigra
Saloop
Sand Pine
Sand Post Oak
Sandhill Post Oak
Sandjack Oak
Sandpaper Oak
Santa Lucia Fir
Santa Rosa Island Torrey Pine
Sapgum
Sapindus Saponaria Var. Drummondii
Sargent Cypress
Sassafras
Sassafras Albidum
Satin-walnut
Savin
Scalybark Hickory
Scarlet Maple
Scarlet Oak
Schneck Oak
Scots Pine
Scrub Holly
Scrub Interior Live Oak
Scrub Live Oak
Scrub Oak
Scrub Pine
Scrub-bay
Scrubby Post Oak
Scythe-leaved Willow
Sequoia Sempervirens
Sequoiadendron Giganteum
Shadblow
Shadbush
Shagbark Hickory
Shasta Fir
Shasta Red Fir
She-balsam
She-oak
Shellbark Hickory
Sheoak
Shin Oak
Shinglewood
Shipmast Locust
Shore Pine
Shorebay
Shortleaf Pine
Shortleaf Yellow Pine
Shortstraw Pine
Shotbush
Shumard Oak
Shumard Red Oak
Shumard's Red Oak
Sierra Alder
Sierra Live Oak
Sierra Lodgepole Pine
Sierra-Cascade Lodgepole Pine
Silkbay
Silver Birch
Silver Fir
Silver Maple
Silver Pine
Silver Spruce
Silvertip Fir
Simmon
Siskiyou Cypress
Sitka Alder
Sitka Cypress
Sitka Spruce
Skunk Spruce
Slash Pine
Slippery Elm
Small-fruited Mountain Ash
Small-seed White Ash
Smelling Stick
Smooth Bebb Willow
Smooth-bark Cypress
Smooth-bark Oak
Smoothbark Hickory
Smoothbark Oak
Soap Berry
Soapberry
Soft Elm
Soft Maple
Soft Pine
Soft-shelled Hickory
Soledad Pine
Sophora Secundiflora
Sorbus Americana
Sorrel-tree
Sourgum
Sourwood
South Florida Slash Pine
Southern Balsam Fir
Southern California Black Walnut
Southern California Walnut
Southern Cypress
Southern Fir
Southern Hackberry
Southern Magnolia
Southern Red Oak
Southern Sweetbay
Southern White-cedar
Southern Yellow Pine
Southwestern Black Willow
Southwestern Locust
Southwestern Peach Willow
Southwestern White Pine
Spanish Oak
Speckled Alder
Spice-tree
Spotted Oak
Spring Birch
Spruce Pine
Staghorn Sumac
Star-leaf Gum
Stave Oak
Stinking Cedar
Stinking Nutmeg
Stinking Yew
Striped Maple
Striped Oak
Subalpine Fir
Subalpine Larch
Sugar Hackberry
Sugar Maple
Sugar Pine
Sugarberry
Sugarplum
Swamp Birch
Swamp Blackgum
Swamp Chestnut Oak
Swamp Cypress
Swamp Hickory
Swamp Holly
Swamp Laurel Oak
Swamp Magnolia
Swamp Oak
Swamp Pine
Swamp Post Oak
Swamp Red Oak
Swamp Spanish Oak
Swamp Tupelo
Swamp White Oak
Swamp Willow
Swamp Willow Oak
Swamp-cedar
Swampbay
Sweet Bean Locust
Sweet Magnolia
Sweet Pecan
Sweet Pignut Hickory
Sweetbay
Sweetgum
Sycamore

Table Mountain Pine
Tag Alder
Tamarack
Tamarack Larch
Tamarack Pine
Tamarix Aphylla
Tan Oak
Tanbark Oak
Tanbark-oak
Tanoak
Tascate
Tasmanian Bluegum
Taxodium Distichum
Taxodium Mucronatum
Taxus Brevifolia
Taxus Floridana
Tecate Cypress
Texas Arbutus
Texas Black Walnut
Texas Cedar
Texas Madrone
Texas Madrono
Texas Mountain Laurel
Texas Oak
Texas Persimmon
Texas Red Oak
Texas Sugarberry
Texas Walnut
Texate
Thin-leaved Alder
Thinleaf Alder
Thuja Occidentalis
Thuja Plicata
Tideland Spruce
Tilia Americana
Timberline Larch
Toothache Tree
Torrey Pine
Torreya Californica
Torreya Taxifolia
Trembling Aspen
Tsuga Canadensis
Tsuga Caroliniana
Tsuga Heterophylla
Tsuga Mertensiana
Tulip-poplar
Tuliptree
Tupelo
Tupelo-gum

Ulmus Americana
Ulmus Rubra
Umbellularia Californica
Una De Gato
Upland Willow Oak

Valley Oak
Valley White Oak
Valley Willow
Vasey Shin Oak
Velvet Mesquite
Velvet Sumac
Vinegar Tree
Virginia Live Oak
Virginia Pine

Walnut
Walter Pine
Walter's Pine
Washington Palm
Washingtonia Filifera
Washoe Pine
Water Birch
Water Elm
Water Oak
Water White Oak
Water-beech
Wavyleaf Alder
Weeping Oak
Weeping Spruce
West Coast Hemlock
West Texas Live Oak
West Virginia Spruce
Western Alder
Western Balsam Fir
Western Black Willow
Western Boxelder
Western Chinkapin
Western Hackberry
Western Hemlock
Western Hophornbeam
Western Red-cedar
Western Redcedar
Western Soapberry
Western Spruce
Western White Pine
Western White Spruce
Western Yellowpine
Western Yew
Weymouth Pine
Whiplash Willow
Whistlewood
Whistling Pine
White Alder
White Ash
White Balsam
White Beech
White Birch
White Cedar
White Cypress
White Elm
White Fir
White Gum
White Hickory
White Locust
White Myrtle
White Oak
White Pine
White Sassafras
White Spruce
White Walnut
White Willow
White-bay
White-cedar
White-laurel
Whiteheart Hickory
Wild Black Cherry
Wild Cherry
Wild China-tree
Wild Chinaberry
Wild Chinatree
Wild Plum
Willow Oak
Winterberry
Wire Birch
Witch-hazel
Wolf Hophornbeam
Woolly Hophornbeam
Woolly Larch
Wright Willow

Yellow Birch
Yellow Butt Oak
Yellow Chestnut Oak
Yellow Cypress
Yellow Gum
Yellow Locust
Yellow Myrtle
Yellow Oak
Yellow Pine
Yellow Plum
Yellow Slash Pine
Yellow Spruce
Yellow Willow
Yellow Wood
Yellow-bark Oak
Yellow-cedar
Yellow-poplar
Yellowbark Oak
Yew
Yew Brush
Yucu-ndatura
'''

flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

session.add(flora_)
session.commit()

flora_ = Flora()
flora_.name = ""
flora_.characteristics = ""

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