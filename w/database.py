from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Text, ForeignKey, Time, desc

#dummied out for time being
from . import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
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
    
class Flora(Base):
    __tablename__ = "flora"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    
class Feature(Base):
    __tablename__ = "features"
    
    id = Column(Integer, primary_key=True)
    name = Column((String)(1024))
    characteristics = Column((String)(1024))
    
Base.metadata.create_all(engine)