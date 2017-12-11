import os, gps, time
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from .database import Base
from w import app

from getpass import getpass
from werkzeug.security import generate_password_hash
from .database import session

manager = Manager(app)
session = gps.gps()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/wild')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    manager.run()