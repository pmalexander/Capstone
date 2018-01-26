#looks in-shape, just remember the secret key isn't the final one, obviously

import os

MAX_SEARCH_RESULTS = 30

#acts as Dev, can't be asked to relabel
class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/wild"
    DEBUG = True
    TESTING = True
    SECRET_KEY = "not a secret"

class TestingConfig(Config):
    TESTING = True
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = False
    
