#looks in-shape, just remember the secret key isn't the final one, obviously

import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/wild"
    DEBUG = True
    TESTING = True
    SECRET_KEY = "not a secret"

class ProductionConfig(Config):
    DEBUG = False
    
class TestingConfig(Config):
    TESTING = True
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True