import os
from flask_script import Manager
from w import app
from flask_migrate import Migrate, MigrateCommand
from w.database import Base

from w.dataseed import read_locations, read_fauna, read_flora, read_feature

manager = Manager(app)
#look over this, this will be written by the Session() on line 21 below, or rather whatever gps app works nowadays
#session = gps.gps()

class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

@manager.command
def seed():
    locations = read_locations("./w/seed/location.src", "#")
    fauna = read_fauna("./w/seed/fauna.src")
    flora = read_fauna("./w/seed/fauna.src")
    
    for location in locations:
        obj = Location(location)
        session.add(obj)
        session.commit()
    

from w.database import session

if __name__ == "__main__":
    manager.run()