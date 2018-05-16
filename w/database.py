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

flo1 = Flora('American Elderberry', 'Your mother smells of them.')
flo2 = Flora('American Grape', 'Jam, jelly, wine, good.')
flo3 = Flora('American Mayapple', 'May or may not be an apple.')
flo4 = Flora('American Persimmon', 'Per simmon of what?')
flo5 = Flora('American Plum', 'Plum...p fruits that are good and good for you.')
flo6 = Flora('Beach Plum', 'Beach bum, beach plum, same thing.')
flo7 = Flora('Black Cherry', 'It is true, it is sweeter.')
flo8 = Flora('Black Raspberry', 'Ditto for these.')
flo9 = Flora('Blueberry', 'They are more purple than blue.')
flo9 = Flora('Buffalo Berry', 'Does not taste like one, I hope.')
flo10 = Flora('Canada Plum', 'See American plum, just a bit milder.')
flo11 = Flora('Canadian Serviceberry', 'Colloquially known as "sugarplum" ... yeah, I am confused too.')
flo12 = Flora('Chokecherry', 'Please be careful.')
flo13 = Flora('Cocoplum', 'Neither coconut or plum, a mystery.')
flo14 = Flora('Concord Grape', '... more jam, jelly, and wine.')
flo15 = Flora('Cranberry', 'Grows in the water... should have been called Waterberry.')
flo16 = Flora('Dewberry', 'Can be mistaken for a blackberry, same family and all that.')
flo17 = Flora('Desert Apricot"', 'Strange, right?')
flo18 = Flora('Huckleberry', 'Named ones have been to known to exist and take human form.')
flo19 = Flora('Raspberry', 'Very tasty, even better if you like chewing on a bunch of seeds.')
flo20 = Flora('Strawberry', 'The ubiquitous berry, from the vine to your fruit salad or milkshake.')
flo21 = Flora('Corn', 'Amazing plant, tastes good roasted, baked, boiled, and popped with a healthy helping of butter. Can be pretty colorful too!')
flo22 = Flora('Fir Tree', 'Not to be confused with fur.')
flo23 = Flora('Oak Tree', 'Strong wood, sometimes of the professor variety of popular franchises.')
flo24 = Flora('Pine Tree', 'Smell good, so good that people keep them in cars.')
flo25 = Flora('Abies Amabilis', 'A tree.')
flo26 = Flora('Abies Bracteata', '')
flo27 = Flora('Abies Fraseri', '')
flo28 = Flora('Abies Lasiocarpa', '')
flo29 = Flora('Abies Magnifica', '')
flo30 = Flora('Abies Procera', '')
flo31 = Flora('Acer Macrophyllum', '')
flo32 = Flora('Acer Negundo', '')
flo33 = Flora('Acer Pensylvanicum', '')
flo34 = Flora('Acer Rubrum', '')
flo35 = Flora('Acer Saccharinum', '')
flo36 = Flora('Aesculus Californica', '')
flo37 = Flora('Ague Tree', '')
flo38 = Flora('Ahuehuete', '')
flo39 = Flora('Alaska Cedar', '')
flo40 = Flora('Alaska Cypress', '')
flo41 = Flora('Alaska Yellow-cedar', '')
flo42 = Flora('Alaska-cedar', '')
flo43 = Flora('Alaskan Larch', '')
flo44 = Flora('Alberta Spruce', '')
flo45 = Flora('Alberta White Spruce', '')
flo46 = Flora('Allegheny Chinkapin', '')
flo47 = Flora('Alligator-tree', '')
flo48 = Flora('Almond Willow', '')
flo49 = Flora('Alnus Incana Subspecies Rugosa', '')
flo50 = Flora('Alnus Incana Subspecies Tenuifolia', '')
flo51 = Flora('Alnus Rhombifolia', '')
flo52 = Flora('Alnus Rubra', '')
flo53 = Flora('Alnus Viridis Subspecies Crispa', '')
flo54 = Flora('Alnus Viridis Subspecies Sinuata', '')
flo55 = Flora('Alpine Fir', '')
flo56 = Flora('Alpine Hemlock', '')
flo57 = Flora('Alpine Larch', '')
flo58 = Flora('Amabilis Fir', '')
flo59 = Flora('Amelanchier Arborea', '')
flo60 = Flora('American Basswood', '')
flo61 = Flora('American Beech', '')
flo62 = Flora('American Elm', '')
flo63 = Flora('American Green Alder', '')
flo64 = Flora('American Hackberry', '')
flo65 = Flora('American Holly', '')
flo66 = Flora('American Hophornbeam', '')
flo67 = Flora('American Larch', '')
flo68 = Flora('American Mountain-ash', '')
flo69 = Flora('American Plum', '')
flo70 = Flora('American Sycamore', '')
flo71 = Flora('American Walnut', '')
flo72 = Flora('Angelica Tree', '')
flo73 = Flora('Apache Pine', '')
flo74 = Flora('Aralia Spinosa', '')
flo75 = Flora('Arbor Vitae', '')
flo76 = Flora('Arbutus Arizonica', '')
flo77 = Flora('Arbutus Menziesii', '')
flo78 = Flora('Arbutus Texana', '')
flo79 = Flora('Arce - Spanish', '')
flo80 = Flora('Arizona Black Walnut', '')
flo81 = Flora('Arizona Cypress', '')
flo82 = Flora('Arizona Fir', '')
flo83 = Flora('Arizona Longleaf Pine', '')
flo84 = Flora('Arizona Madrone', '')
flo85 = Flora('Arizona Oak', '')
flo86 = Flora('Arizona Rough Cypress', '')
flo87 = Flora('Arizona Walnut', '')
flo88 = Flora('Arizona White Oak', '')
flo89 = Flora('Arkansas Pine', '')
flo90 = Flora('Arkansas Soft Pine', '')
flo91 = Flora('Ash-leaved Maple', '')
flo92 = Flora('Ashe Juniper', '')
flo93 = Flora('Asimina Triloba', '')
flo94 = Flora('Aspen', '')
flo95 = Flora('Athel Tamarisk', '')
flo96 = Flora('Atlantic White-cedar', '')
flo97 = Flora('Australian-pine', '')
flo98 = Flora('Austrian Pine', '')
flo99 = Flora('Baker Cypress', '')
flo100 = Flora('Bald Cypress', '')
flo101 = Flora('Balsam', '')
flo102 = Flora('Balsam Fir', '')
flo103 = Flora('Balsam Fraser Fir', '')
flo104 = Flora('Balsam Poplar', '')
flo105 = Flora('Banks Pine', '')
flo106 = Flora('Banksian Pine', '')
flo107 = Flora('Barren Oak', '')
flo108 = Flora('Basket Oak', '')
flo109 = Flora('Basswood', '')
flo110 = Flora('Bay', '')
flo111 = Flora('Bay Laurel', '')
flo112 = Flora('Baytree', '')
flo113 = Flora('Beach Pine', '')
flo114 = Flora('Beak Willow', '')
flo115 = Flora('Bearberry', '')
flo116 = Flora('Beaverwood', '')
flo117 = Flora('Bebb Willow', '')
flo118 = Flora('Beech', '')
flo119 = Flora('Bellota', '')
flo120 = Flora('Betula Alleghaniensis', '')
flo121 = Flora('Betula Nigra', '')
flo122 = Flora('Betula Occidentalis', '')
flo123 = Flora('Betula Papyrifera', '')
flo124 = Flora('Betula Populifolia', '')
flo125 = Flora('Big Drunk Bean', '')
flo126 = Flora('Big-cone Pine', '')
flo127 = Flora('Big-laurel', '')
flo128 = Flora('Big-leaf Maple', '')
flo129 = Flora('Bigcone Douglas-fir', '')
flo130 = Flora('Bigcone Douglas-spruce', '')
flo131 = Flora('Bigcone Spruce', '')
flo132 = Flora('Bigleaf Maple', '')
flo133 = Flora('Bigtooth Aspen', '')
flo134 = Flora('Bigtree', '')
flo135 = Flora('Biltmore Ash', '')
flo136 = Flora('Biltmore White Ash', '')
flo137 = Flora('Bishop Pine', '')
flo138 = Flora('Bitter Cherr', '')
flo139 = Flora('Bitternut', '')
flo140 = Flora('Bitternut Hickory', '')
flo141 = Flora('Black Birch', '')
flo142 = Flora('Black Hemlock', '')
flo143 = Flora('Black Hills Spruce', '')
flo144 = Flora('Black Jack Oak', '')
flo145 = Flora('Black Locust', '')
flo146 = Flora('Black Myrtle', '')
flo147 = Flora('Black Oak', '')
flo148 = Flora('Black Pine', '')
flo149 = Flora('Black Tupelo', '')
flo150 = Flora('Black Walnut', '')
flo151 = Flora('Black Willow', '')
flo152 = Flora('Blackgum', '')
flo153 = Flora('Blackjack Oak', '')
flo154 = Flora('Blisted', '')
flo155 = Flora('Blister Fir', '')
flo156 = Flora('Blue Oak', '')
flo157 = Flora('Blue Paloverde', '')
flo158 = Flora('Blue Spruce', '')
flo159 = Flora('Blue-beech', '')
flo160 = Flora('Blue-poplar', '')
flo161 = Flora('Bluegum', '')
flo162 = Flora('Bluegum Eucalyptus', '')
flo163 = Flora('Bluejack Oak', '')
flo164 = Flora('Bois D-arc', '')
flo165 = Flora('Border Limber Pine', '')
flo166 = Flora('Border Pinyon', '')
flo167 = Flora('Border White Pine', '')
flo168 = Flora('Bottom White Pine', '')
flo169 = Flora('Bottomland Post Oak', '')
flo170 = Flora('Bottomland Red Oak', '')
flo171 = Flora('Boxelder', '')
flo172 = Flora('Boynton Post Oak', '')
flo173 = Flora('Bracted Balsam Fir', '')
flo174 = Flora('Brake Cedar', '')
flo175 = Flora('Brewer Spruce', '')
flo176 = Flora('Bristlecone Fir', '')
flo177 = Flora('Broadleaf Maple', '')
flo178 = Flora('Broom Hickory', '')
flo179 = Flora('Buckeye', '')
flo180 = Flora('Bull Pine', '')
flo181 = Flora('Bull-bay', '')
flo182 = Flora('Bullnut', '')
flo183 = Flora('Bur Oak', '')
flo184 = Flora('Butternut', '')
flo185 = Flora('Buttonball Tree', '')
flo186 = Flora('Cabbage Palmetto', '')
flo187 = Flora('California Bay', '')
flo188 = Flora('California Black Walnut', '')

session.add(flo1)
session.add(flo2)
session.add(flo3)
session.add(flo4)
session.add(flo5)
session.add(flo6)
session.add(flo7)
session.add(flo8)
session.add(flo9)
session.add(flo10)
session.add(flo11)
session.add(flo12)
session.add(flo13)
session.add(flo14)
session.add(flo15)
session.add(flo16)
session.add(flo17)
session.add(flo18)
session.add(flo19)
session.add(flo20)
session.add(flo21)
session.add(flo22)
session.add(flo23)
session.add(flo24)
session.add(flo25)
session.add(flo26)
session.add(flo27)
session.add(flo28)
session.add(flo29)
session.add(flo30)
session.add(flo31)
session.add(flo32)
session.add(flo33)
session.add(flo34)
session.add(flo35)
session.add(flo36)
session.add(flo37)
session.add(flo38)
session.add(flo39)
session.add(flo40)
session.add(flo41)
session.add(flo42)
session.add(flo43)
session.add(flo44)
session.add(flo45)
session.add(flo46)
session.add(flo47)
session.add(flo48)
session.add(flo49)
session.add(flo50)
session.add(flo51)
session.add(flo52)
session.add(flo53)
session.add(flo54)
session.add(flo55)
session.add(flo56)
session.add(flo67)
session.add(flo68)
session.add(flo69)
session.add(flo70)
session.add(flo71)
session.add(flo72)
session.add(flo73)
session.add(flo74)
session.add(flo75)
session.add(flo76)
session.add(flo77)
session.add(flo78)
session.add(flo79)
session.add(flo80)
session.add(flo81)
session.add(flo82)
session.add(flo83)
session.add(flo84)
session.add(flo85)
session.add(flo86)
session.add(flo87)
session.add(flo88)
session.add(flo89)
session.add(flo90)
session.add(flo91)
session.add(flo92)
session.add(flo93)
session.add(flo94)
session.add(flo95)
session.add(flo96)
session.add(flo97)
session.add(flo98)
session.add(flo99)
session.add(flo100)
session.add(flo101)
session.add(flo102)
session.add(flo103)
session.add(flo104)
session.add(flo105)
session.add(flo106)
session.add(flo107)
session.add(flo108)
session.add(flo109)
session.add(flo110)
session.add(flo111)
session.add(flo112)
session.add(flo113)
session.add(flo114)
session.add(flo115)
session.add(flo116)
session.add(flo117)
session.add(flo118)
session.add(flo119)
session.add(flo120)
session.add(flo121)
session.add(flo122)
session.add(flo123)
session.add(flo124)
session.add(flo125)
session.add(flo126)
session.add(flo127)
session.add(flo128)
session.add(flo129)
session.add(flo130)
session.add(flo131)
session.add(flo132)
session.add(flo133)
session.add(flo134)
session.add(flo135)
session.add(flo136)
session.add(flo137)
session.add(flo138)
session.add(flo139)
session.add(flo140)
session.add(flo141)
session.add(flo142)
session.add(flo143)
session.add(flo144)
session.add(flo145)
session.add(flo146)
session.add(flo147)
session.add(flo148)
session.add(flo149)
session.add(flo150)
session.add(flo151)
session.add(flo152)
session.add(flo153)
session.add(flo154)
session.add(flo155)
session.add(flo156)
session.add(flo157)
session.add(flo158)
session.add(flo159)
session.add(flo160)
session.add(flo161)
session.add(flo162)
session.add(flo163)
session.add(flo164)
session.add(flo165)
session.add(flo166)
session.add(flo167)
session.add(flo168)
session.add(flo169)
session.add(flo170)
session.add(flo171)
session.add(flo172)
session.add(flo173)
session.add(flo174)
session.add(flo175)
session.add(flo176)
session.add(flo177)
session.add(flo178)
session.add(flo179)
session.add(flo180)
session.add(flo181)
session.add(flo182)
session.add(flo183)
session.add(flo184)
session.add(flo185)
session.add(flo186)
session.add(flo187)
session.add(flo188)

session.commit()

##############
###FEATURES###
##############

# adds features and provide descriptions of landmarks/features endemic to each location, these can be associated with specific locations (parks)
# descriptions are not final, just for flavor and fun at the moment until more accurate descriptors (taxonomy, attractions, natural formations, historical creations and all that) can be issued in a timely manner

fea1 = Feature('Petrified Wood', 'Really hard and really old wood endemic, but not exclusive to, the Petrified Forest National Park')
fea2 = Feature('Balanced Rock', 'A precariously placed (by nature) rock that sits atop another rock in Garden of the Gods, do not sleep underneath it.')
fea3 = Feature('Old Faithful', 'An old geyser, spurts reliably, located in Yellowstone National Park.')
fea4 = Feature('Grand Prismatic Spring', 'Giant colorful natural spring found in Yellowstone National Park.')
fea5 = Feature('Cadillac Mountain', 'Not a new car model, but the highest point on the Atlantic Coast.')
fea6 = Feature('Havasu Falls', 'A colorful and scenic diversion found in the Grand Canyon, as well as an opportunity to get wet.')
fea7 = Feature('High Dune', 'No worries about wormsign, the High Dune is 30 miles wide and has some of the highest dunes in North America, it is located in the appropriately named Great Sand Dunes National Park and Preserve.')
fea8 = Feature('Harding Icefield Trail', 'Pack and prepare for nearly 8 miles of trail on a glacial path at a glacial or not-so glacial pace in Kenjai Fords National Park.')
fea9 = Feature('The Narrows', 'Aptly named as it is the narrowest stretch during your hike in Zion Canyon at the Zion National Park.')
fea10 = Feature('Landscape Arch', 'Not falling, nor golden, but a group of naturally formed arches at Arches National Park.')
fea11 = Feature('Tunnel View Overlook', 'A good view of Yosemite National Park attractions, Half Dome, Bridalveil Fall and El Capitan.')
fea12 = Feature('The General Sherman Tree', 'Unlike Union Army general of its namesake, this tree does not appreciate fire, but is also a historical standout in being the largest tree in the world, located right in Sequoia National Park.')
fea13 = Feature('Crater Lake', 'Just as the name implies, it is a crater lake. Formed by an eruption from a now inactive volcano a long, long, long, time ago, to be the deepest lake in the United States. Located in the appropirately named Crater Lake National Park.')
fea14 = Feature('Highline Trail', 'A high-elevation trail in Glacier National Park, with a good view of the mountain peaks and valleys, unless you are acrophobic, in which case it gives a good view of fear.')
fea15 = Feature('Mount Kilauea', 'This notorious and extremely volatile active volcano is located in the Hawaii Volcanoes National Park, busy producing up to 500,000 cubic meters of lava per day. Do not get too close.')
fea16 = Feature('Hoh Rain Forest', 'Figured your compass turned you wrong? Nope, this rainforest is a part of Olympic National Park attractions, representative of a temperate rainforest biome located in North America.')
fea17 = Feature('Bryce Amphitheater', 'A 6-mile stretch of Bryce Canyon National Park features a series of spires, eerily colorful a different points of the day, and invoking the image of a crowd of individuals standing shoulder to shoulder.')

session.add(fea1)
session.add(fea2)
session.add(fea3)
session.add(fea4)
session.add(fea5)
session.add(fea6)
session.add(fea7)
session.add(fea8)
session.add(fea9)
session.add(fea10)

session.commit()