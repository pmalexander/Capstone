from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Text, ForeignKey, Time, desc

#dummied out for time being
from . import app

engine = create_engine(app.config["postgresql://ubuntu:thinkful@localhost:5432/wild"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

import gps, os, time
import datetime
from datetime import datetime

class Location(Base):
    __tablename__ = "locations"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    latitude = Column(Float)
    longitude = Column(Float)
    visitors = Column(Integer)
    
class Fauna(Base):
    __tablename__ = "fauna"
    
    id = Column 
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    
    assoc_fauna = relationship("Location", backref="assoc_fauna")
    
class Flora(Base):
    __tablename__ = "flora"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    
    assoc_flora = relationship("Location", backref="assoc_flora")
    
class Feature(Base):
    __tablename__ = "features"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    
    assoc_feature = relationship("Location", backref="assoc_feature")
    
#adds national park/reserves to be queried in database, latitude and longitude of location saved
park_1 = Location()
park_1.name = "Blue Ridge Parkway"
latitude = 36.659089
longitude = -81.077139
park_1.visitors = "15000"
 
session.add(park_1)
session.commit()

#adds fauna and provide descriptions of fauna, these can be associated with specific locations
black_bear = Fauna()
black_bear.name = "Black Bear"
black_bear.description = "They are often found in areas with relatively inaccessible terrain, thick understory vegetation and large quantities of edible material (especially masts). The adaptation to woodlands and thick vegetation in this species may have originally been due to the black bear having evolved alongside larger, more aggressive bear species, such as the extinct short-faced bear and the still living grizzly bear, that monopolized more open habitats and the historic presence of larger predators such as smilodon and the American lion that could have preyed on black bears. Although found in the largest numbers in wild, undisturbed areas and rural regions, black bears can adapt to surviving in some numbers in peri-urban regions as long as they contain easily accessible foods and some vegetative coverage."

session.add(black_bear)
session.commit()

#adds flora and provide descriptions of fauna, these can be associated with specific locations
fir_tree = Flora()
fir_tree = "Fir Tree"
fir_tree = "Firs are most closely related to the genus Cedrus (cedar). Douglas firs are not true firs, being of the genus Pseudotsuga. hey are large trees, reaching heights of 10–80 m (33–262 ft) tall and trunk diameters of 0.5–4 m (1 ft 8 in–13 ft 1 in) when mature. Firs can be distinguished from other members of the pine family by the unique attachment of their needle-like leaves and by their different cones."

session.add(black_bear)
session.commit()

#adds features and provide descriptions of fauna, these can be associated with specific locations (parks)
feature_stream = Feature()
feature_stream = "Stream"
feature_stream = "A stream is a body of water[1] with a current, confined within a bed and banks. Streams are important as conduits in the water cycle, instruments in groundwater recharge, and corridors for fish and wildlife migration."

session.add(feature_stream)
session.commit()

Base.metadata.create_all(engine)