import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/wild"
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Thor'

class ProductionConfig(Config):
    DEBUG = False
    
class TestingConfig(Config):
    TESTING = True
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True